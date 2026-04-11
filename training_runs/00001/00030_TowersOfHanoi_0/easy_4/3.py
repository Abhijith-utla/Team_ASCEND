def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        if rods[j][-1] == min(rods[j]):
            return False
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8]

assert sat([])
assert not sat([[0, 0]])
assert not sat([[0, 1]])
assert sat([[0, 0], [1, 1]])
assert not sat([[0, 0], [0, 1]])
assert sat([[0, 0], [1, 1], [2, 2]])
assert not sat([[0, 0], [1, 1], [1, 2]])
assert sat([[0, 0], [1, 1], [2, 2], [3, 3]])
assert not sat([[0, 0], [1, 1], [2, 2], [4, 4]])
assert sat([[0, 0], [1, 1], [2, 2], [3, 3], [5, 5]])
assert not sat([[0, 0], [1, 1], [2

if __name__ == "__main__":
    assert sat(sol())
