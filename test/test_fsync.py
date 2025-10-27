import os, time

with open("data.txt", "w", encoding="utf-8") as f:
    f.write("HELLO FROM FSYNC\n")
    f.flush()
    os.fsync(f.fileno())  # ensure physical write
    print("Flushed and fsynced (durable), waiting...")
    time.sleep(10)
