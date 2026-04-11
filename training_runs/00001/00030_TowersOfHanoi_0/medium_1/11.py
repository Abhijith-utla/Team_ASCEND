def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return []

assert sat([])
assert not sat([[0, 6]])
assert not sat([[0, 1], [1, 0]])
assert not sat([[6, 4]])
assert not sat([[6, 4], [5, 7]])
assert not sat([[5, 7], [6, 4]])
assert sat([[1, 2]])
assert not sat([[1, 3], [2, 0]])
assert not sat([[2, 3], [0, 6]])
assert not sat([[2, 0], [1, 3]])
assert not sat([[2, 1], [3, 6]])
assert not sat([[3, 6], [2, 7]])
assert not sat([[3, 7], [0, 4]])
assert not sat([[4, 0], [3, 5]])
assert not sat([[4, 5], [3, 2]])
assert not sat([[4,

if __name__ == "__main__":
    assert sat(sol())
