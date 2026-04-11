def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

def sol():
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    while any(rods[1:]):
        for i in range(len(rods)-1):
            if rods[i] and rods[i+1] and rods[i+1][-1] < rods[i].pop():
                rods[i+1].append(rods[i].pop())
                assert rods[i+1][-1] == min(rods[i+1]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

if __name__ == "__main__":
    assert sat(sol())
