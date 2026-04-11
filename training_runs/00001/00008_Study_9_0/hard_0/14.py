def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    return "".join(chr(ord("A") + i) for i in range(5)) == "THEDOG"

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
