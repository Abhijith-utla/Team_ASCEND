def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

def sol():
    def sat(li: List[int]):
        return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

    assert sat([])
    assert not sat([1, 2, 2, 3, 4, 5, 6, 7, 8, 9])
    assert not sat([2, 3, 5, 7, 11, 13, 17, 19, 23])
    assert sat([1, 1, 1, 2, 2, 2, 3, 3, 3])
    assert not sat([1, 2, 3, 4, 4, 4, 5, 5, 5])
    assert sat([1, 2, 3, 4, 4, 5, 6, 7, 8])
    assert not sat([1, 2, 2, 3, 3, 4, 5, 6, 6])

if __name__ == "__main__":
    assert sat(sol())
