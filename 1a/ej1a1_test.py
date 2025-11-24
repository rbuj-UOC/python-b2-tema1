from ej1a1 import text_to_bytes, reverse_bytes, increment_bytearray_rollover, bytes_to_text


def test_text_to_bytes():
    assert text_to_bytes("Hello") == b"Hello", "Should encode text to bytes"

def test_reverse_bytes():
    assert reverse_bytes(b"Hello")[0] == ord("o"), "The first byte should be the last character's ASCII value"

def test_increment_bytearray_rollover():
    byte_array = bytearray([255, 0, 1, 254])
    incremented = increment_bytearray_rollover(byte_array)
    assert incremented == bytearray([0, 1, 2, 255]), "Should increment each byte and rollover at 256"

def test_bytes_to_text():
    assert bytes_to_text(b"Hello") == "Hello", "Should decode bytes to text"
