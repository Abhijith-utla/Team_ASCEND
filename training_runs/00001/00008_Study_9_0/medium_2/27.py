def sat(li: List[int]):
    return [i for i in li if i >= 0] == list(
        "The five boxing wizards jump quickly".split(" "))

def sol():
    return [i for i in [1, 2, -1, 3, -3, 5] if i >= 0]

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
