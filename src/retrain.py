import subprocess, sys

# Gate retrain behind validation again (safety)
steps = [
    [sys.executable, "src/validate.py"],
    [sys.executable, "src/train.py"],
]

if __name__ == "__main__":
    for s in steps:
        ret = subprocess.call(s)
        if ret != 0:
            print("Step failed:", s)
            sys.exit(ret)
    print("✅ Retrain complete; production model updated.")
