def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

def sol():
    return []

assert sat([])
assert sat([[1, 0]])
assert sat([[0, 1]])
assert sat([[0, 1], [1, 0]])
assert sat([[2, 0]])
assert sat([[0, 1], [1, 2]])
assert sat([[1, 2]])
assert sat([[0, 1], [2, 1]])
assert sat([[1, 0], [2, 0]])
assert sat([[2, 1]])
assert sat([[0, 1], [2, 0]])
assert sat([[0, 2]])
assert sat([[1, 0], [2, 1]])
assert sat([[2, 0]])
assert sat([[1, 0], [2, 2]])
assert sat([[2, 2]])
assert sat([[0, 2], [1, 1]])
assert sat([[1, 1]])
assert sat([[0,

if __name__ == "__main__":
    assert sat(sol())
