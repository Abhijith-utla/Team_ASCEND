def sat(li: List[int]):
    return all(x >= 0 and 2 ** x - 1 == (2 ** x) - 1 for x in li)

def sol():
    def sat(li: List[int]):
        return all(x >= 0 and 2 ** x - 1 == (2 ** x) - 1 for x in li)

    assert sat([-1, 0, 1, 2, 3])
    assert not sat([-1, 0, 1, 3])
    assert not sat([-1, 1, 1, 1])
    assert sat([0, 1, 2, 3, 5])
    assert not sat([-1, -2, -3])
    assert sat([-10, -9, -8, -7, -6])

sol()

if __name__ == "__main__":
    assert sat(sol())
