from pydantic import BaseModel, Field
from typing import Optional, List
import os
from pathlib import Path
import glob

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
        
        if not self.valves.project_root:
            return "Error: project_root Valve is not configured. Please set it in the tool settings."

        # CONTRACT: Path Isolation (prevent directory traversal)
        safe_filename = os.path.basename(filename)
        root_path = Path(self.valves.project_root).resolve()
        
        # Define search priority tiers
        # Tier 1: Root
        # Tier 2: High-probability mentor/docs folders
        # Tier 3: Recursive discovery
        search_tiers = [
            root_path / safe_filename,
            root_path / "mentor" / safe_filename,
            root_path / "docs" / safe_filename,
        ]
        
        # 1. Try Tier 1 & 2 (Direct hits)
        for path in search_tiers:
            if path.exists() and path.is_file():
                return self._read_file_safely(path)

        # 2. Tier 3: Prioritized Recursive Search
        # We use a glob search but filter out 'noise' directories to avoid finding 
        # old versions in .git, data, or checkpoints.
        BANNED_DIRS = {'.git', 'data', '__pycache__', '.ipynb_checkpoints', 'venv', 'node_modules'}
        
        try:
            # Search recursively for the filename
            all_matches = list(root_path.rglob(safe_filename))
            
            # Filter matches: remove any path that contains a banned directory
            valid_matches = [
                path for path in all_matches 
                if not any(banned in path.parts for banned in BANNED_DIRS)
            ]
            
            if valid_matches:
                # Return the first valid match found (sorted by depth to prefer shallower paths)
                best_match = min(valid_matches, key=lambda p: len(p.parts))
                return self._read_file_safely(best_match)
                
        except Exception as e:
            return f"Error during recursive search: {str(e)}"

        return f"Error: Critical mentor file '{safe_filename}' not found in root, mentor/, docs/, or via filtered recursive search."

    def _read_file_safely(self, path: Path) -> str:
        """Internal helper to handle file reading and encoding."""
        try:
            # Ensure we are still within the root path (final safety check)
            if not str(path.resolve()).startswith(str(Path(self.valves.project_root).resolve())):
                return "Security Error: Attempted to read file outside of project root."
                
            return path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            return f"Error: File at {path} is not a valid UTF-8 text file."
        except Exception as e:
            return f"Error reading file: {str(e)}"
