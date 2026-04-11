def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[i].append(rods[j].pop())
        if rods[i][-1] < min(rods[i]):
            rods[i].append(rods[j].pop())
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for i, j in moves:
        rods[i].append(rods[j].pop())
        if rods[i][-1] < min(rods[i]):
            rods[i].append(rods[j].pop())
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

moves = [(0,1), (1,2), (2,1), (3,0), (2,3), (3,2), (0,3), (1,0), (2,2), (1,1)]
assert sat(moves)

if __name__ == "__main__":
    assert sat(sol())
