from pydantic import BaseModel, Field
from typing import Optional, List
import os
from pathlib import Path
import glob

class Valves(BaseModel):
    project_root: str = Field(
        default="",
        description="The absolute path to the project root directory for critical file retrieval. MUST be configured in the UI."
    )

class Tools:
    """
    Mentor Critical Retrieval Tool

    This tool is strictly reserved for the Mentor persona to retrieve mandated 'Source of Truth'
    documents (e.g., syllabus.md, user_profile.md) required for session protocols.

    CONTRACTS:
    1. Determinism: Given the same project_root and filename, the tool must return the same file.
    2. Isolation: The tool must never access files outside the project_root.
    3. Prioritization: The tool must prioritize known 'Source of Truth' directories over general search.
    4. Noise Reduction: Recursive searches must ignore technical/data directories (.git, data, etc.).
    """

    class Valves(BaseModel):
        project_root: str = Field(
            default="",
            description="The absolute path to the project root directory for critical file retrieval. MUST be configured in the UI."
        )

    # The crucial injection hook for Open WebUI backend
    valves = Valves()

    def __init__(self):
        # Ensure valves attribute exists to prevent AttributeError if injection fails
        if not hasattr(self, 'valves'):
            self.valves = Valves()

    def get_mentor_critical_file(self, filename: str) -> str:
        """
        Deterministically retrieves a critical mentor source-of-truth file.
        This is NOT a general file reader; it is optimized for finding course artifacts.

        :param filename: The exact name of the file to retrieve (e.g., 'syllabus.md').
        :return: The full text content of the file or a descriptive error message.
        """
        # CONTRACT: Input Validation
        if not filename or not isinstance(filename, str):
            return "Error: A valid filename string must be provided."

        # DIAGNOSTIC: Check the actual state of the object
        valves = getattr(self, 'valves', None)
        if not valves or not valves.project_root:
            debug_info = f"Object Type: {type(self)} | Has 'valves' attr: {'valves' in dir(self)} | valves value: {valves}"
            return f"Reason: project_root Valve is not configured. [DEBUG]: {debug_info}. Action: Please set the project_root in Open WebUI tool settings."

        # CONTRACT: Path Isolation (prevent directory traversal)
        safe_filename = os.path.basename(filename)
        try:
            root_path = Path(valves.project_root).resolve()
        except Exception as e:
            return f"Reason: Invalid project_root path. Error: {str(e)}. Action: Correct the path in Tool Valves."

        # Track attempted paths for diagnostics
        attempted_paths = []

        # Define search priority tiers
        search_tiers = [
            root_path / safe_filename,
            root_path / "mentor" / safe_filename,
            root_path / "docs" / safe_filename,
        ]

        # 1. Try Tier 1 & 2 (Direct hits)
        for path in search_tiers:
            attempted_paths.append((str(path), path.exists()))
            if path.exists() and path.is_file():
                return self._read_file_safely(path)

        # 2. Tier 3: Prioritized Recursive Search
        BANNED_DIRS = {'.git', 'data', '__pycache__', '.ipynb_checkpoints', 'venv', 'node_modules'}

        try:
            all_matches = list(root_path.rglob(safe_filename))
            
            # Diagnostic: Log all matches found before filtering
            found_raw = [str(p) for p in all_matches]

            valid_matches = [
                path for path in all_matches
                if not any(banned in path.parts for banned in BANNED_DIRS)
            ]

            if valid_matches:
                best_match = min(valid_matches, key=lambda p: len(p.parts))
                return self._read_file_safely(best_match)
            
            # Build diagnostic report for recursive failure
            recursive_info = f"Raw matches: {found_raw if found_raw else 'None'} | Valid matches after filter: {len(valid_matches)}"

        except Exception as e:
            return f"Error during recursive search: {str(e)}"

        # FINAL DIAGNOSTIC REPORT: Detailed failure analysis
        path_summary = "\n".join([f"- {p}: {'EXISTS' if e else 'MISSING'}" for p, e in attempted_paths])
        debug_report = (
            f"\n[DIAGNOSTIC TRACE]\n"
            f"Project Root: {root_path}\n"
            f"Target File: {safe_filename}\n"
            f"Direct Checks:\n{path_summary}\n"
            f"Recursive Search: {recursive_info}\n"
            f"CWD: {os.getcwd()}\n"
            f"User: {os.getlogin() if hasattr(os, 'getlogin') else 'unknown'}"
        )
        
        return f"Reason: Critical mentor file '{safe_filename}' not found. Action: Verify the file exists in the project root or mentor/ directory.{debug_report}"

    def _read_file_safely(self, path: Path) -> str:
        """Internal helper to handle file reading and encoding."""
        try:
            # Open WebUI injects valves as an attribute. Handle case where it might be missing.
            valves = getattr(self, 'valves', None)
            if not valves or not valves.project_root:
                return "Reason: valves configuration missing during file read. Action: Configure tool valves."

            # Ensure we are still within the root path (final safety check)
            if not str(path.resolve()).startswith(str(Path(valves.project_root).resolve())):
                return "Reason: Security breach - attempted to read outside project root. Action: Halt immediately."

            return path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            return f"Error: File at {path} is not a valid UTF-8 text file."
        except Exception as e:
            return f"Error reading file: {str(e)}"
