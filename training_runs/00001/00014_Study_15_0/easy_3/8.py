def sat(li: List[int]):
    return all(x >= 0 and 2 ** x - 1 == (2 ** (x + 1)) - 1 for x in li)

def sol():
    def sat(li: List[int]):
        return all(x >= 0 and 2 ** x - 1 == (2 ** (x + 1)) - 1 for x in li)

    return sat([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

if __name__ == "__main__":
    assert sat(sol())
