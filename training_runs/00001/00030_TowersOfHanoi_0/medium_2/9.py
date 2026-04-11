def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    moves = [
        [0, 6],
        [1, 5],
        [0, 4],
        [3, 2],
        [1, 3],
        [2, 4],
        [0, 3],
        [4, 0],
        [5, 1],
        [6, 2],
        [7, 3],
        [4, 7],
        [6, 5],
        [7, 6],
        [3, 4]
    ]
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

if __name__ == "__main__":
    assert sat(sol())
