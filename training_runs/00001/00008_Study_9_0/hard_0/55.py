def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    li = [13, 21, 3]
    return [chr(ord('a') + i) for i in li] == list("the")

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
