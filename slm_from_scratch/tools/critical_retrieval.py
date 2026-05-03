from pydantic import BaseModel, Field
from typing import Optional
import os

class Tools:
    class Valves(BaseModel):
        project_root: str = Field(
            default="",
            description="The absolute path to the project root directory for critical file retrieval. MUST be configured in the UI."
        )

    def get_critical_file(self, filename: str) -> str:
        """
        Deterministically retrieves the content of a critical source-of-truth file (e.g., 'syllabus.md', 'user_profile.md').
        Use this tool when the RAG system fails to provide the exact content of a mandated project file.

        :param filename: The exact name of the file to retrieve (e.g., 'syllabus.md').
        :return: The full text content of the file or an error message if not found.
        """
        # Ensure the filename is just a name, not a path to prevent directory traversal
        safe_filename = os.path.basename(filename)
        file_path = os.path.join(self.valves.project_root, safe_filename)

        # Check common sub-directories if not found in root
        search_paths = [
            file_path,
            os.path.join(self.valves.project_root, "mentor", safe_filename),
            os.path.join(self.valves.project_root, "docs", safe_filename),
        ]

        for path in search_paths:
            if os.path.exists(path) and os.path.isfile(path):
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        return f.read()
                except Exception as e:
                    return f"Error reading file {path}: {str(e)}"

        return f"Error: Critical file '{safe_filename}' not found in root or mentor directories."
