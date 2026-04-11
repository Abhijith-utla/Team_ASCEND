def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[i].append(rods[j].pop())
        if rods[i][-1] == min(rods[i]):
            rods[i].append(rods[j].pop())
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8]

# Testing the solution
assert sat([])
assert not sat([[0, 7]])
assert sat([[0, 6], [1, 5]])
assert not sat([[0, 1]])
assert sat([[1, 3]])
assert sat([[0, 1], [1, 2]])
assert not sat([[0, 7]])
assert sat([[1, 5]])
assert not sat([[2, 7]])
assert sat([[0, 6], [1, 5]])
assert not sat([[2, 7]])
assert sat([[0, 6], [1, 5], [2, 7]])
assert not sat([[0, 1]])
assert not sat([[0, 7]])
assert not sat([[0, 6], [1, 5], [2, 7], [3, 8]])
assert not

if __name__ == "__main__":
    assert sat(sol())
