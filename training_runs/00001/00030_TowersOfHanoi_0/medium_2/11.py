def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return []

if __name__ == "__main__":
    assert sat([])
    assert sat([[0, 1]])
    assert sat([[0, 1], [1, 0]])
    assert sat([[0, 1], [1, 2]])
    assert sat([[0, 1], [1, 2], [2, 3]])
    assert sat([[0, 1], [1, 2], [2, 3], [3, 2]])
    assert sat([[0, 1], [1, 2], [2, 3], [3, 4]])
    assert sat([[0, 1], [1, 2], [2, 3], [3, 4], [4, 3]])
    assert sat([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]])
    assert sat([[0, 1], [1, 2], [2, 3], [3,

if __name__ == "__main__":
    assert sat(sol())
