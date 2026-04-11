def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[i].append(rods[j].pop(0))
        assert rods[i][-1] == min(rods[i]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return []

# Test cases
assert sat([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]])
assert not sat([[0, 1], [1, 2], [2, 3], [3, 4], [5, 4]])
assert sat([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
assert not sat([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [7, 8]])

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
