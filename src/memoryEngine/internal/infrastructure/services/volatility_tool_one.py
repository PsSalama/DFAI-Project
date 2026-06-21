import subprocess
import json
import os


def run_volatility(file_path: str, plugin: str) -> dict:
    output_dir = "dumps"
    os.makedirs(output_dir, exist_ok=True)

    # 1. Run volatility with the JSON output engine renderer flag
    command = ["vol", "-f", file_path, "-r", "json", "-o", "dumps/", plugin]
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(f"Volatility failed: {result.stderr}")

    try:
        # This is the list of dictionaries that was causing your mapper to crash!
        raw_volatility_list = json.loads(result.stdout)

        # 2. Flatten that list of key-value row blocks into one single master dictionary
        flattened_dictionary = {}
        for item in raw_volatility_list:
            key = item.get("Variable")
            value = item.get("Value")

            if key is not None:
                # If the value is a memory address integer, format it cleanly to hex string
                if isinstance(value, int) and "version" not in key.lower() and "processors" not in key.lower():
                    flattened_dictionary[key] = hex(value)
                else:
                    flattened_dictionary[key] = str(value)

        # 3. Return the dictionary so the mapper can run `.get()` safely!
        return flattened_dictionary

    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to decode Volatility JSON output: {e}")