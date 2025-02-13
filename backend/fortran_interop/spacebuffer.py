def space_buffer(string: str) -> bytes:
    spaces  = " " * (128-len(string))
    string += spaces
    return string.encode()
