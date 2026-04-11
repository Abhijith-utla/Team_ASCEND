def sat(li: List[int]):
    return [chr(i) for i in li] == list("The quick brown fox jumps over the lazy dog".replace(" ", ""))

def sol():
    return [chr(i) for i in range(97, 123)]

if __name__ == "__main__":
    assert sat(sol())
