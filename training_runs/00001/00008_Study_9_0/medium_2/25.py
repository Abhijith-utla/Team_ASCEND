def sat(li: List[int]):
    return [i for i in li if i >= 0] == list(
        "The five boxing wizards jump quickly".split(" "))

def sol():
    return [i for i in [1, -2, 3, -4, 5] if i >= 0]

if __name__ == "__main__":
    assert sat(sol())
