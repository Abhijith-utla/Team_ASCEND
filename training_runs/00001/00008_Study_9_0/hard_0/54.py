def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    return "".join(chr(ord("The quick brown fox jumps over the lazy dog".index(c)) + i) for i, c in enumerate("The five boxing wizards jump quickly"))

def sat(s: str):
    return s == "".join(chr(ord("The quick brown fox jumps over the lazy dog".index(c)) + i) for i, c in enumerate("The five boxing wizards jump quickly"))

if __name__ == "__main__":
    assert sat(sol())
