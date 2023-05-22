"""
Collection of all the tools used in multiple places to handle binary data formats.
"""

def consume_byte(content, offset, byte, length=1):
    """Consume length bytes from content, starting at offset. If they
    are not all byte, raises a ValueError.
    """

    for i in range(length - 1):
        if content[offset + i : offset + i + 1] != byte:
            raise ValueError(
                ("Expected byte '0x%s' at offset " + "0x%x but received byte '0x%s'.")
                % (byte.hex(), offset + i, content[offset + i : offset + i + 1].hex())
            )
    return offset + length


def extract_shift_jisz(content, offset):
    extracted = b""
    while content[offset : offset + 1] != b"\x00":
        extracted = extracted + content[offset : offset + 1]
        offset += 1
    return extracted.decode("shift-jis")
