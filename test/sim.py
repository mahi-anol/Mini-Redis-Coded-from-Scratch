import subprocess
import time
import os
import platform
import signal

def crash_process(proc):
    """Cross-platform process killer."""
    if platform.system() == "Windows":
        proc.terminate()  # Windows equivalent of SIGKILL
    else:
        os.kill(proc.pid, signal.SIGKILL)
    print("💥 Process killed!")

def run_test(script_name):
    print(f"\n=== Running {script_name} ===")
    # Remove previous file
    if os.path.exists("data.txt"):
        os.remove("data.txt")

    # Start test script
    proc = subprocess.Popen(["python", script_name])
    time.sleep(3)  # wait until file is written but not yet flushed/fsynced
    crash_process(proc)
    time.sleep(1)  # give OS time to release handles

    if os.path.exists("data.txt"):
        with open("data.txt", "r", encoding="utf-8") as f:
            content = f.read()
        print(f"📄 File content after crash ({script_name}):\n{repr(content)}")
    else:
        print(f"🚫 No file found after crash for {script_name}.")

# Test all cases
for script in ["test_write.py", "test_flush.py", "test_fsync.py"]:
    run_test(script)
