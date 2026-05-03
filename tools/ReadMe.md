# Open WebUI Tools

This directory contains custom Python tools designed to extend the capabilities of the SLM Mentor. These tools are designed to be loaded into [Open WebUI](https://openwebui.com).

## 🛠️ mentor_critical_retrieval.py

This tool provides the mentor with a deterministic way to retrieve critical "Source of Truth" files (like `syllabus.md` or `user_profile.md`) directly from the local filesystem, bypassing the probabilistic nature of RAG to eliminate `[RETRIEVAL BREACH]` errors.

### ⚠️ Important: Not a General File Reader
This tool is **not** a general-purpose `read_file` utility. It implements a **Prioritized Search Strategy** and **Strict Path Isolation** to ensure the mentor always retrieves the *active* version of the syllabus or user profile, rather than an archived or backup copy.

### How to Register the Tool

1.  **Login to Open WebUI**: Open your local Open WebUI instance in the browser.
2.  **Navigate to Tools**: Go to **Workspace** $\rightarrow$ **Tools**.
3.  **Import the Tool**:
    *   Click the **+** (plus) button or the **Import** button.
    *   Upload the `mentor_critical_retrieval.py` file from this directory.
4.  **Configure the Path (Crucial)**:
    *   Once imported, find the **Mentor Critical Retrieval** tool in the list.
    *   Click the **Gear Icon ($\text{⚙️}$)** to open the **Valves** (Settings).
    *   In the `project_root` field, enter the **absolute path** to your project root directory.
    *   *Example:* `/home/user/projects/slm_from_scratch`
    *   **Save** the settings.
5.  **Assign to Model**:
    *   Go to **Workspace** $\rightarrow$ **Models**.
    *   Edit the **SLM Mentor** model.
    *   In the **Tools** section, select the **Mentor Critical Retrieval** tool.
    *   **Save** the model.

### 🔍 Prioritized Search Logic

To prevent "Ambiguity" (finding an old backup of a file), the tool searches in this order:
1. **Direct Root**: Checks if the file is in the root.
2. **High-Probability Folders**: Checks `mentor/` and `docs/`.
3. **Filtered Recursive Search**: Searches the entire project but explicitly ignores "Noise" directories (`.git`, `data`, `venv`, `.ipynb_checkpoints`) to prevent retrieving outdated versions.


### 📂 Handling Multiple Projects

This tool is configured for a **single project root** via its Valve. If you are working across multiple projects (e.g., `slm_from_scratch` and `ai_engineering_book`), each with its own `syllabus.md`, you cannot use one global tool instance for all of them.

**The recommended workaround is the "Siloed Tool" approach:**

1.  **Duplicate the Tool**: Upload the `critical_retrieval.py` file multiple times with different names (e.g., `slm_retrieval.py`, `book_retrieval.py`).
2.  **Specific Configuration**: Configure the `project_root` Valve for each tool to point to its respective project directory.
3.  **Scoped Assignment**:
    *   Assign the `slm_retrieval` tool only to the **SLM Mentor** model.
    *   Assign the `book_retrieval` tool only to the **Book Architect** model.
    *   Or, assign them to specific **Folders/Collections** in Open WebUI.

This ensures that the agent always retrieves the `syllabus.md` from the project context it is currently operating in.

### 🔒 Security Note

To prevent leaking your local file system structure to public repositories (e.g., GitHub), the tool does **not** hardcode your file paths.

The absolute path is stored exclusively in the Open WebUI database via the `project_root` Valve. Never add your absolute paths directly into the `.py` file before committing.

## 🐳 Infrastructure & Determinism: Podman/Docker and SELinux

If you are running Open WebUI in a container (e.g., via `podman run` or `docker run`), the tools are executed within the container's filesystem (`/app/backend`), not directly on your host. This creates a filesystem isolation gap.

### 1. Volume Mounting (The Visibility Gap)
To allow the tool to see your host files, you **must** mount the project root into the container. To avoid configuration churn, mount the host path to the identical path inside the container.

**Example (Podman/Docker CLI):**
```bash
podman run -v /path/to/your/project:/path/to/your/project:Z ...
```

### 2. SELinux Labeling (The Permission Gap)
On systems with SELinux enabled (e.g., Fedora, RHEL), a successful mount is not enough. You will encounter `[Errno 13] Permission denied` because the container process is not authorized to access the host's security labels.

**The Fix:** Use the `:Z` flag in your volume mapping to automatically relabel the files for container access. This is critical for Podman users on Fedora/RHEL.

**Correct Mount Flag:**
`-v /path/to/host:/path/to/container:Z`

### 3. The "Binary Gate" Protocol
The Mentor is configured with a **Binary Gate**. If the deterministic retrieval tool fails to find the syllabus or profile (due to misconfiguration or mount failure), the Mentor is **forbidden** from falling back to RAG or internal training data. It will report a `[RETRIEVAL BREACH]` and halt, ensuring 100% fidelity to the course map.
