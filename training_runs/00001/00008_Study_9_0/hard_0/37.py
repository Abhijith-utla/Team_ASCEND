def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    return ["The quick brown fox jumps over the lazy dog"[i] for i in [1, 2, 3, 4, 5]] == list(
        "The five boxing wizards jump quickly")

if __name__ == "__main__":
    assert sat(sol())
