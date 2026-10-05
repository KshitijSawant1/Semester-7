import subprocess
import sys
from pathlib import Path

# test_nlp.py is inside Practicals/NLP
BASE_DIR = Path(__file__).parent

print("=" * 60)
print("NLP PRACTICAL TEST RUNNER")
print("=" * 60)

passed = []
failed = []
missing = []

for i in range(1, 10):

    name = f"Exp {i}"
    file = BASE_DIR / name / "code.py"

    print(f"\n{'=' * 60}")
    print(f"Testing {name}")
    print("=" * 60)

    if not file.exists():
        print("[MISSING]", file)
        missing.append(name)
        continue

    try:
        result = subprocess.run(
            [sys.executable, str(file)],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.stdout:
            print(result.stdout)

        if result.returncode == 0:
            print(f"[PASS] {name}")
            passed.append(name)

        else:
            print(f"[FAIL] {name}")
            print(result.stderr)
            failed.append(name)

    except subprocess.TimeoutExpired:
        print(f"[FAIL] {name} - Timeout")
        failed.append(name)


print("\n" + "=" * 60)
print("FINAL NLP PRACTICAL TEST REPORT")
print("=" * 60)

print("Total Experiments :", 9)
print("Passed            :", len(passed))
print("Failed            :", len(failed))
print("Missing           :", len(missing))

print()

for i in range(1, 10):
    name = f"Exp {i}"

    if name in passed:
        status = "PASS"
    elif name in failed:
        status = "FAIL"
    else:
        status = "MISSING"

    print(f"{name:<10} : {status}")

print("=" * 60)