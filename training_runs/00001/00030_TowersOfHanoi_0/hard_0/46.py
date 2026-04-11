def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

def sol():
    moves = []
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for i in range(8):
        moves.append([i, i+1])
        rods[0].append(rods[1].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

print(sol())

if __name__ == "__main__":
    assert sat(sol())
