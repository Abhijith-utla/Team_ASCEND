def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return [8, 7, 6, 5, 4, 3, 2, 1]

assert sat([])
assert sat([[0, 7]])
assert sat([[0, 6], [1, 7]])
assert sat([[0, 5], [1, 6], [2, 7]])
assert sat([[0, 4], [1, 5], [2, 6], [3, 7]])
assert sat([[0, 3], [1, 4], [2, 5], [3, 6]])
assert sat([[0, 2], [1, 3], [2, 4], [3, 5]])
assert sat([[0, 1], [1, 2], [2, 3], [3, 4]])
assert sat([[0, 0]])
assert sat([[1, 0]])
assert sat([[2, 0]])
assert sat([[3, 0]])
assert sat([[4,

if __name__ == "__main__":
    assert sat(sol())
