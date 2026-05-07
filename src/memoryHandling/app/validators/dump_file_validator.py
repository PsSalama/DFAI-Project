import os
import hashlib
from dataclasses import dataclass

@dataclass
class ValidationResult:
    is_valid: bool
    message: str = ""
    normalized_path: str = ""
    file_size: int = 0
    sha256: str = ""

class DumpFileValidator:
    ALLOWED_EXTENSIONS = {".vmem", ".mem", ".dmp", ".raw"}

    @staticmethod
    def _calculate_sha256(path: str) -> str:
        sha256_hash = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                sha256_hash.update(chunk)

        return sha256_hash.hexdigest()

    @staticmethod
    def validate(path: str) -> ValidationResult:
        # 1. basic check
        if not path or not path.strip():
            return ValidationResult(False, "Path is empty")

        # 2. normalize path (IMPORTANT FIX)
        path = path.strip()

        # 3. check exists
        if not os.path.exists(path):
            return ValidationResult(False, "File does not exist")

        # 4. check file type
        if not os.path.isfile(path):
            return ValidationResult(False, "Path is not a file")

        # 5. extension validation (fixed)
        _, ext = os.path.splitext(path)
        ext = ext.lower()

        if ext not in DumpFileValidator.ALLOWED_EXTENSIONS:
            return ValidationResult(False, f"Invalid file extension: '{ext}'")

        # 6. permission check
        if not os.access(path, os.R_OK):
            return ValidationResult(False, "File is not readable")

        # 7. size validation (basic sanity check)
        file_size = os.path.getsize(path)
        if file_size < 1024:  # 1 KB minimum (adjust if needed)
            return ValidationResult(False, "File too small to be a valid dump")

        # 8. optional integrity hash (for tracking / forensics)
        sha256 = DumpFileValidator._calculate_sha256(path)

        return ValidationResult(
            is_valid=True,
            message="Valid dump file",
            normalized_path=path,
            file_size=file_size,
            sha256=sha256
        )