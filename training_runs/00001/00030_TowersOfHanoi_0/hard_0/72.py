def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

def sol():
    return [8, 7, 6, 5, 4, 3, 2, 1]

assert sat([])
assert sol() == [8, 7, 6, 5, 4, 3, 2, 1]
assert sat([[0, 7], [1, 6], [2, 5], [3, 4]])
assert sol() == []
assert sol() != [1, 2, 3, 4, 5, 6, 7, 8]
assert not sat([[6, 0], [5, 1], [4, 2], [3, 3]])
assert sol() == []

if __name__ == "__main__":
    assert sat(sol())
