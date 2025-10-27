import time

with open("data.txt", "w", encoding="utf-8") as f:
    f.write("HELLO FROM WRITE\n")
    print("Wrote data but not flushed yet...")
    time.sleep(10)  # give time before crash
