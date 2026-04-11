def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    return "".join([chr(ord('a') + i) for i in range(26)])

if __name__ == "__main__":
    assert sat(sol())
