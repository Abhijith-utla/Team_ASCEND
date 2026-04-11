def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        if rods[j][-1] == min(rods[j]):
            return False
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return []

# Adding some moves to test the solution
moves = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 0]]
assert sat(moves)

moves = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [0, 7]]
assert not sat(moves)

if __name__ == "__main__":
    assert sat(sol())
