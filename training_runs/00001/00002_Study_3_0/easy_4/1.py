def sat(li: List[int]) -> bool:
    return sorted(li) == list(range(len(li))) and all(li[i] == i for i in range(len(li)))

def sol():
    return sorted([1, 2, 3, 4, 5]) == list(range(1, 6)) and all([x == i for i, x in enumerate([1, 2, 3, 4, 5])])

def test():
    assert sat(sol())
    assert not sat(sol([1, 2, 4, 3, 5]))
    assert not sat(sol([1, 2, 3, 5, 4]))
    assert not sat(sol([5, 4, 3, 2, 1]))

test()

if __name__ == "__main__":
    assert sat(sol())
