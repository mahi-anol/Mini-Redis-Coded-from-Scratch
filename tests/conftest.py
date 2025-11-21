import pytest
import subprocess
import time
import socket
import sys

HOST = "127.0.0.1"
PORT = 6379

@pytest.fixture(scope="session", autouse=True)
def redis_server():
    """Start the Redis server before tests and stop after."""
    process = subprocess.Popen([sys.executable, "main.py"])
    time.sleep(0.5)  # wait for server to start
    yield process
    process.terminate()
    process.wait()


def redis_client():
    """Open a socket connection to the server."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    return s


def send_command(cmd: str) -> str:
    """Send a raw Redis/RESP command and return response."""
    s = redis_client()
    s.sendall(cmd.encode())
    data = s.recv(4096)
    s.close()
    return data.decode()
