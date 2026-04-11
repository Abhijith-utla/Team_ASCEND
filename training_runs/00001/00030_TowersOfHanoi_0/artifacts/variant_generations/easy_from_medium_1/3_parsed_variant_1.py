def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop(0))
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
