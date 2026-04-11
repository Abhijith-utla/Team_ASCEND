def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[i].append(rods[j].pop())
        if rods[i][-1] == min(rods[i]):
            rods[i].pop()
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return [[1, 2, 3, 4, 5, 6, 7, 8]]

# Testing the function
assert sat([])
assert not sat([[8, 7, 6, 5, 4, 3, 2, 1]])
assert not sat([[1, 2, 3, 5, 4], [1, 2, 3, 4, 5]])
assert sat([[1, 2, 3, 5, 4], [0, 1]])
assert sat([[3, 2, 1, 5, 4], [0, 1]])
assert sat([[1, 2, 3, 4, 5, 6, 7, 8], [0, 1]])
assert not sat([[8, 7, 6, 5, 4, 3, 2, 1], [0, 1]])

if __name__ == "__main__":
    assert sat(sol())
