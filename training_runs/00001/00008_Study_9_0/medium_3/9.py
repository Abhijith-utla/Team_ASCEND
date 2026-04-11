def sat(li: List[int]):
    return [chr(i) for i in li] == list(
        "The quick brown fox jumps over the lazy dog".replace(" ", ""))

def sol():
    li = [ord(i) for i in "The quick brown fox jumps over the lazy dog"]
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
