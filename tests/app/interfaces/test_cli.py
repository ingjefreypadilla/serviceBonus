import subprocess
import sys

def run_cli(args):
    result = subprocess.run(
        [sys.executable, "main.py"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def test_cli_output_for_alice():
    output = run_cli(["--name", "Alice", "--years", "12", "--salary", "3000"])
    assert "Worker: Alice" in output
    assert "Service bonus: $1800.00" in output

def test_cli_output_with_cap():
    output = run_cli(["--name", "Carol", "--years", "25", "--salary", "4000"])
    assert "Worker: Carol" in output
    assert "Service bonus: $4000.00" in output