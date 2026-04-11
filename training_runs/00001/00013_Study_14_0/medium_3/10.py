def sat(li: List[int]):
    return all([i == sum(li[j] for j in range(i+1, len(li))) for i in range(len(li))])

def sol():
    def sat(li: List[int]):
        return all([i == sum(li[j] for j in range(i+1, len(li))) for i in range(len(li))])

    assert sat([])
    assert not sat([1, 2, 3])
    assert sat([1, 2, 3, 6, 10, 15])
    assert not sat([1, 2, 4, 6, 10, 15])
    assert sat([1])
    assert not sat([2, 4, 6, 8, 10, 12])
    assert sat([1, 2, 4, 6, 8, 10, 12])
    assert not sat([2, 3, 4, 6, 8, 10, 12])
    assert sat([1, 2, 3, 4, 6, 8, 10, 12])
    assert not sat([1, 2, 3, 4,

if __name__ == "__main__":
    assert sat(sol())
