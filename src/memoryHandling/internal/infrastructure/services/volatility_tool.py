import subprocess
import json, os

def run_volatility(file_path: str, plugin: str) -> list[dict]:
    output_dir = "dumps"
    os.makedirs(output_dir, exist_ok=True)

    command = ["vol", "-f", file_path, "-r", "json", "-o", "dumps/", plugin]
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(f"Volatility failed: {result.stderr}")

    # Convert the raw JSON output string directly into a Python list of dicts
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to decode Volatility JSON output: {e}")