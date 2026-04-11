def sat(li: List[int]):
    return [chr(i) for i in li] == list("The quick brown fox jumps over the lazy dog".replace(" ", ""))

def sol():
    return "".join(chr(i) for i in range(32, 127))

if __name__ == "__main__":
    assert sat(sol())
