def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    return [ord(s) for s in "The quick brown fox jumps over the lazy dog" if s in "aeiouAEIOU"]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
