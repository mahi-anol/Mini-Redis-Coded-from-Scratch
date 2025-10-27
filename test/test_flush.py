import time

with open("data.txt", "w", encoding="utf-8") as f:
    f.write("HELLO FROM FLUSH\n")
    f.flush()  # flushed to OS cache
    print("Flushed to OS cache, waiting...")
    time.sleep(10)
