def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

def sol():
    moves = [(2, 1), (5, 2), (3, 1), (6, 3), (4, 2)]
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for i, j in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

if __name__ == "__main__":
    assert sat(sol())
