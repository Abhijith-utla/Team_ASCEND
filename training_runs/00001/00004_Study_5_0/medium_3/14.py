def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)]) and li.count(0) == 1

def sol():
    def sat(li: List[int]):
        return all([li.count(i) == i for i in range(10)]) and li.count(0) == 1

    assert sat([])
    assert sat([0])
    assert not sat([1])
    assert not sat([0, 0])
    assert sat([1, 1, 1])
    assert sat([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert not sat([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    assert not sat([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0])
    assert sat([0]*10)
    assert sat([1]*9 + [0])
    assert sat([0]*10 + [1])
    assert sat([0]*5 + [1]*5

if __name__ == "__main__":
    assert sat(sol())
