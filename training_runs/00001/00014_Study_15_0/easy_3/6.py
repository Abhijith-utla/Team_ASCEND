def sat(li: List[int]):
    return all(x >= 0 and 2 ** x - 1 == (2 ** (x + 1)) - 1 for x in li)

def sol():
    return sat([1, 2, 3, 4, 5])

def sat(li: List[int]):
    return all(x >= 0 and 2 ** x - 1 == (2 ** (x + 1)) - 1 for x in li)

if __name__ == "__main__":
    assert sat(sol())
