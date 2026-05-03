# Open WebUI Tools

This directory contains custom Python tools designed to extend the capabilities of the SLM Mentor. These tools are designed to be loaded into [Open WebUI](https://openwebui.com).

## 🛠️ critical_retrieval.py

This tool provides the mentor with a deterministic way to retrieve critical "Source of Truth" files (like `syllabus.md` or `user_profile.md`) directly from the local filesystem, bypassing the probabilistic nature of RAG to eliminate `[RETRIEVAL BREACH]` errors.

### How to Register the Tool

1.  **Login to Open WebUI**: Open your local Open WebUI instance in the browser.
2.  **Navigate to Tools**: Go to **Workspace** $\rightarrow$ **Tools**.
3.  **Import the Tool**:
    *   Click the **+** (plus) button or the **Import** button.
    *   Upload the `critical_retrieval.py` file from this directory.
4.  **Configure the Path (Crucial)**:
    *   Once imported, find the **Critical Retrieval** tool in the list.
    *   Click the **Gear Icon ($\text{⚙️}$)** to open the **Valves** (Settings).
    *   In the `project_root` field, enter the **absolute path** to your project root directory.
    *   *Example:* `/home/user/projects/slm_from_scratch`
    *   **Save** the settings.
5.  **Assign to Model**:
    *   Go to **Workspace** $\rightarrow$ **Models**.
    *   Edit the **SLM Mentor** model.
    *   In the **Tools** section, select the **Critical Retrieval** tool.
    *   **Save** the model.

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
