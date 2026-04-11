def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    li = [ord(i) - ord('a') for i in "The quick brown fox jumps over the lazy dog"]
    return li

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
