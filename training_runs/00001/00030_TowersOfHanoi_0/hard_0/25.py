def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

def sol():
    moves = [(4, 0), (1, 1), (3, 2), (5, 3), (2, 4), (6, 4)]
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for i, j in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

# Test the solution
def test_sol():
    assert sat(moves)

test_sol()

if __name__ == "__main__":
    assert sat(sol())
