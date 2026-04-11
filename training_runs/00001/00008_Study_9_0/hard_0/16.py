def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    return "".join(["The quick brown fox jumps over the lazy dog"[i] for i in [i for i in range(len("The quick brown fox jumps over the lazy dog"))]])

if __name__ == "__main__":
    assert sat(sol())
