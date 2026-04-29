import subprocess

def process(file_path, output_path):
    result = subprocess.run(
        ["vol", "-f", file_path, "windows.pslist"],
        capture_output=True,
        text=True
    )
    # Save output to file
    with open("resources/"+output_path, "w", encoding="utf-8") as f:
        f.write(result.stdout)
    return result.stdout
