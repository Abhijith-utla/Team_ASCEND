def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[i].append(rods[j].pop())
        assert rods[i][-1] == min(rods[i]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return []

def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[i].append(rods[j].pop())
        assert rods[i][-1] == min(rods[i]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

assert sat([])
assert not sat([[0, 0]])
assert not sat([[0, 1]])
assert sat([[0, 0], [1, 1]])
assert not sat([[0, 1], [0, 0]])
assert sat([[0, 0], [1, 1], [1, 2], [0, 1], [1, 0]])

if __name__ == "__main__":
    assert sat(sol())
