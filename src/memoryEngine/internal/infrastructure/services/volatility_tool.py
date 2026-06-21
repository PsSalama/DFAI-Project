import subprocess
import json
import os
import logging

logger = logging.getLogger(__name__)


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

    try:
        raw_data = json.loads(result.stdout)

        # SCHEMA TYPE 1: Direct flat list of object records (e.g., pslist, hivelist)
        if isinstance(raw_data, list):
            return raw_data

        # SCHEMA TYPE 2: Complex dictionary metadata block (e.g., consoles, cmdscan)
        if isinstance(raw_data, dict):
            columns = [col["name"] for col in raw_data.get("columns", [])]
            rows = raw_data.get("rows", [])

            normalized_records = []
            for row in rows:
                # Map column header names explicitly to row array items
                record = dict(zip(columns, row))
                normalized_records.append(record)

            return normalized_records

        # Catch unexpected structural fallback elements
        logger.warning(f"Volatility returned an unhandled data type: {type(raw_data)}")
        return []

    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to decode Volatility JSON output: {e}")