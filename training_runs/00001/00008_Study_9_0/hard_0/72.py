def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    return [ord(c) for c in "The quick brown fox jumps over the lazy dog" if c in "The quick brown fox jumps over the lazy dog"] == [ord(c) for c in "The five boxing wizards jump quickly"]

if __name__ == "__main__":
    assert sat(sol())
