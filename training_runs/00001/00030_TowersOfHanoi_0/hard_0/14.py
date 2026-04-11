def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

def sol():
    return []

# Test case
moves = [(0, 1), (1, 2), (2, 0), (0, 2)]
assert sat(moves) == [2, 3, 1, 0]

# Additional test cases
moves = [(3, 1), (1, 2), (2, 0), (0, 2)]
assert sat(moves) == [3, 1, 2, 0]

moves = [(1, 0), (2, 1), (0, 2), (1, 3)]
assert sat(moves) == [1, 0, 2, 3]

moves = [(0, 1), (2, 0), (1, 2), (3, 1)]
assert sat(moves) == [0, 1, 2, 3]

moves = [(0, 2), (1, 0), (2, 1), (3, 2)]
assert sat(moves) == [0

if __name__ == "__main__":
    assert sat(sol())
