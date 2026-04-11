def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    li = [ord(c) for c in "The quick brown fox jumps over the lazy dog"]
    assert sat(li)
    return "".join([chr(i) for i in li])

if __name__ == "__main__":
    assert sat(sol())
