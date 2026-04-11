def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return [8, 7, 6, 5, 4, 3, 2, 1]

assert sat([])
assert not sat([[0, 6]])
assert not sat([[1, 6]])
assert sat([[0, 6], [1, 5]])
assert not sat([[0, 5], [1, 6]])
assert not sat([[1, 6], [0, 7]])
assert sat([[0, 6], [1, 7]])
assert not sat([[0, 7], [1, 6]])
assert not sat([[0, 5], [1, 7]])
assert not sat([[0, 6], [0, 7]])
assert sat([[0, 6], [1, 7], [2, 8]])
assert not sat([[0, 7], [1, 6], [2, 8]])
assert not sat([[0, 6], [0, 7]])
assert sat([[0

if __name__ == "__main__":
    assert sat(sol())
