def sat(li: List[int]):
    return all([sum(li[:i]) == i for i in range(20)])

def sol():
    def sat(li: List[int]):
        return all([sum(li[:i]) == i for i in range(20)])

    assert sat([])
    assert not sat([1])
    assert sat([1, 1])
    assert not sat([1, 2])
    assert sat([1, 2, 3])
    assert not sat([1, 2, 4])
    assert sat([1, 2, 3, 6])
    assert not sat([1, 2, 3, 7])
    assert sat([1, 2, 3, 5, 8])
    assert not sat([1, 2, 3, 6, 9])
    assert sat([1, 2, 3, 5, 7, 10])
    assert not sat([1, 2, 3, 5, 6, 11])
    assert sat([1, 2, 3, 4, 8, 12])
    assert not sat([1, 2, 3

if __name__ == "__main__":
    assert sat(sol())
