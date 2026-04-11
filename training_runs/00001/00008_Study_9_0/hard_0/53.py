def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    return "".join(list("The quick brown fox jumps over the lazy dog")[i] for i in [1, 3, 15, 6, 9, 4, 11, 7, 8, 0, 14, 10, 12, 16, 5, 2, 13])

print(sol())

if __name__ == "__main__":
    assert sat(sol())
