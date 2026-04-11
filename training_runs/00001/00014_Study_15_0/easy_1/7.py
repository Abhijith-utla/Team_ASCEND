def sat(li: List[int]):
    return all(x >= 0 and 2 ** x - 1 == (2 ** x) - 1 for x in li)

def sol(li: List[int]):
    return all(x >= 0 and 2 ** x - 1 == (2 ** x) - 1 for x in li)

if __name__ == "__main__":
    assert sat(sol())
