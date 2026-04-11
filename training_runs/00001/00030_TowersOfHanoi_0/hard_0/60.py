def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

def sol():
    moves = []
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    while rods[2] or rods[1] or rods[0]:
        i = rods[1].pop(0)
        if rods[2] and rods[2][0] < i:
            rods[2].insert(0, rods[2].pop())
        else:
            rods[0].insert(0, i)
        moves.append([rods[1].pop(0), rods[2].pop(0) if rods[2] else None])
    return moves

if __name__ == "__main__":
    assert sat(sol())
