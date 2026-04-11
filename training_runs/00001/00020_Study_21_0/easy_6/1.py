def sat(li: List[int]):
    return all(li[i] != li[i + 1] for i in range(8) if len(set(li)) == 3)

def sol():
    def sat(li: List[int]):
        return all(li[i] != li[i + 1] for i in range(8) if len(set(li)) == 3)

    assert sat([1, 2, 3, 4, 5, 6, 7, 8])
    assert not sat([1, 2, 3, 4, 5, 6, 6, 7])
    assert not sat([1, 2, 3, 4, 5, 6, 7, 7])
    assert not sat([1, 1, 1, 2, 2, 2, 3, 3])
    assert sat([1, 2, 3, 4, 5, 6, 7, 8])
    assert not sat([1, 2, 3, 4, 5, 5, 6, 7])
    assert not sat([1, 1, 1, 1, 2, 2, 2, 3])
    assert not sat

if __name__ == "__main__":
    assert sat(sol())
