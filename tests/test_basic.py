from conftest import send_command

def test_set_get():
    # SET a key
    resp = send_command("SET a 5\r\n")
    assert "+OK" in resp

    # GET the key
    resp = send_command("GET a\r\n")
    assert "$1\r\n5\r\n" in resp
