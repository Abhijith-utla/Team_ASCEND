def sat(li: List[int]):
    return [ord(i) for i in li] == list(
        "The five boxing wizards jump quickly".replace(" ", ""))

def sol(li: List[int]):
    return [ord(i) for i in li] == list(
        "".join(e for e in "The five boxing wizards jump quickly" if e.isalnum()))

if __name__ == "__main__":
    assert sat(sol())
