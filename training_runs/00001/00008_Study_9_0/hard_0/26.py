def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    return [ord(i) for i in "The quick brown fox jumps over the lazy dog"][:len("The quick brown fox jumps over the lazy dog")] == list(
        "The five boxing wizards jump quickly")

if __name__ == "__main__":
    assert sat(sol())
