def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[j].insert(0, rods[i].pop())
        if rods[j][-1] == min(rods[j]):
            return False
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    return rods

if __name__ == "__main__":
    assert sat(sol())
