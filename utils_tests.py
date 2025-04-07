import subprocess

def run_test(input_path, source, expected_output):
    process = subprocess.run(
        ["php", "interpret.php", f"--input={input_path}"],
        input=source,
        capture_output=True,
        text=True,
        timeout=5,
    )

    print(process.stdout)

    assert process.returncode == 0, f"Expected return code 0, but got {process.returncode}"
    
    assert len(process.stderr) == 0
    assert len(process.stdout) != 0

    assert process.stdout.strip() == expected_output.strip(), f"Expected stdout:\n{expected_output}\nGot:\n{process.stdout}"
