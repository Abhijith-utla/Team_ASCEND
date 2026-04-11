def sat(li: List[int]):
    return all(sum(li[:i]) == 2 ** i - 1 for i in range(20))

def sol():
    def sat(li: List[int]):
        return all(sum(li[:i]) == 2 ** i - 1 for i in range(20))

    assert sat([])
    assert sat([1])
    assert not sat([1, 2])
    assert sat([1, 1])
    assert sat([1, 1, 1])
    assert not sat([1, 1, 2])
    assert sat([1, 1, 1, 1])
    assert not sat([1, 2, 3, 4])
    assert sat([1, 1, 1, 1, 1])
    assert not sat([1, 2, 3, 4, 5])
    assert sat([1, 1, 1, 1, 1, 1])
    assert not sat([1, 2, 3, 4, 5, 6])
    assert sat([1, 1, 1, 1, 1, 1, 1])
    assert not sat([1, 2

if __name__ == "__main__":
    assert sat(sol())
