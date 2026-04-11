def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10, 0, -1)])

def sol():
    def sat(li: List[int]):
        for i in range(10, 0, -1):
            if li.count(i) != i:
                return False
        return True

    assert sat(list(range(1, 11)))
    assert not sat(list(range(1, 10)))
    assert not sat(list(range(10, 11)))
    assert not sat(list(range(9, 0, -1)))
    assert sat(list(range(9, 10)))

sol()

if __name__ == "__main__":
    assert sat(sol())
