def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    moves = [[0, 6], [1, 5], [0, 4], [3, 2], [2, 1]]
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1], 0)
    for [i, j] in moves:
        rods = (rods[0], [x for x in rods[1] if x != rods[2]], rods[2] + 1, rods[3], [rods[3] + 1, rods[2], rods[1][0]], [rods[1][0]] + [rods[2] + 1, rods[1][1:]])
        if rods[0][-1] == min(rods[0]):
            break
    else:
        return False
    return True

if __name__ == "__main__":
    assert sat(sol())
