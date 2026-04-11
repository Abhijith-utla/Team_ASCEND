def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return []

assert sat([])
assert sat([[1, 0]])
assert sat([[2, 0], [1, 1]])
assert sat([[3, 0], [2, 1], [1, 2]])
assert sat([[4, 0], [3, 1], [2, 2], [1, 3]])
assert sat([[5, 0], [4, 1], [3, 2], [2, 3], [1, 4]])
assert sat([[6, 0], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]])
assert sat([[7, 0], [6, 1], [5, 2], [4, 3], [3, 4], [2, 5], [1, 6]])
assert sat([[8, 0], [7, 1], [6, 2], [5, 3], [4, 4], [3, 5

if __name__ == "__main__":
    assert sat(sol())
