def sat(li: List[int]):
    return all(li[i] != li[i + 1] for i in range(8) if len(set(li)) == 3)

def sol(li: List[int]) -> bool:
    return all(li[i] != li[i + 1] for i in range(8)) and len(set(li)) == 3

def test():
    assert not sol([1, 2, 3, 4, 5, 6, 7, 8])
    assert sol([1, 2, 3, 2, 5, 6, 7, 8])
    assert not sol([1, 2, 3, 4, 5, 5, 7, 8])
    assert sol([1, 2, 3, 4, 5, 6, 7, 7])

test()

if __name__ == "__main__":
    assert sat(sol())
