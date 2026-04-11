def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        if rods[j][-1] == min(rods[j]):
            return False
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return [8, 7, 6, 5, 4, 3, 2, 1]

assert sat([])
assert sat([[0, 0]])
assert sat([[0, 1]])
assert sat([[0, 2]])
assert sat([[0, 3]])
assert sat([[0, 4]])
assert sat([[0, 5]])
assert sat([[0, 6]])
assert sat([[0, 7]])
assert sat([[0, 7], [1, 6]])
assert sat([[0, 7], [1, 7]])
assert sat([[0, 7], [2, 6]])
assert sat([[0, 7], [3, 6]])
assert sat([[0, 7], [4, 6]])
assert sat([[0, 7], [5, 6]])
assert sat([[0, 7], [6, 6]])
assert sat([[0, 7], [7

if __name__ == "__main__":
    assert sat(sol())
