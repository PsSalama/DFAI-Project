import subprocess
import os

OUTPUT_DIR = "resources"


def run_volatility(file_path: str, plugin: str, output_file: str) -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    result = subprocess.run(
        ["vol", "-f", file_path, plugin],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Volatility failed for {plugin}: {result.stderr}"
        )
    output_path = os.path.join(OUTPUT_DIR, output_file)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result.stdout)
    return output_path
