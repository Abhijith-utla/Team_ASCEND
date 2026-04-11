def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

def sol():
    return []

assert sat([])
assert not sat([[0, 0]])
assert not sat([[0, 1]])
assert not sat([[0, 2]])
assert not sat([[0, 3]])
assert not sat([[0, 4]])
assert not sat([[0, 5]])
assert not sat([[0, 6]])
assert not sat([[0, 7]])
assert not sat([[0, 8]])
assert not sat([[1, 0]])
assert not sat([[1, 1]])
assert not sat([[1, 2]])
assert not sat([[1, 3]])
assert not sat([[1, 4]])
assert not sat([[1, 5]])
assert not sat([[1, 6]])
assert not sat([[1, 7]])
assert not sat([[1, 8]])
assert not sat([[2, 0]])
assert not sat([[2, 1]])
assert

if __name__ == "__main__":
    assert sat(sol())
