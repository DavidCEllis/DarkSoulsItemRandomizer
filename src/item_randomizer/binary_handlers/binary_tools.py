"""
Collection of all the tools used in multiple places to handle binary data formats.
"""

def consume_byte(content, offset, byte, length=1):
    """Consume length bytes from content, starting at offset. If they
    are not all byte, raises a ValueError.
    """

    for i in range(length - 1):
        data = content[offset + i : offset + i + 1]
        if data != byte:
            raise ValueError(
                ("Expected byte '0x%s' at offset " + "0x%x but received byte '0x%s'.")
                % (byte.hex(), offset + i, content[offset + i : offset + i + 1].hex())
            )
    return offset + length


def read_until_terminator(
        content: bytes,
        offset: int,
        *,
        terminator: bytes=b"\x00",
) -> bytes:
    extracted: list[bytes] = []
    for char in content[offset:]:
        if char == terminator:
            break
        else:
            extracted.append(char)
    else:
        raise ValueError(
            "Reached the end of content without finding a termination char."
        )
    return b"".join(extracted)

def extract_decode(content, offset, *, codec="utf-8", terminator=b"\x00"):
    extracted = read_until_terminator(content, offset, terminator=terminator)
    return extracted.decode(codec)


def extract_shift_jisz(content, offset):
    return extract_decode(content, offset, codec="shift-jis")


def extract_strz(content, offset):
    return extract_decode(content, offset, codec="utf-8")
