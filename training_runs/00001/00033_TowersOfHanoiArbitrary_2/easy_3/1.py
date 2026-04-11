def sat(moves: List[List[int]], source=[[0, 1, 2], [3], [4, 5, 6]], target=[[1, 2, 3], [4, 5], [0, 6]]):
    state = [s[:] for s in source]
    for move in moves:
        i, j = move[0], move[1]
        state[i].insert(j, state[j].pop(0))
    return state == target

def sol():
    return []

assert sat([])
assert not sat([[0, 1, 2], [3], [4, 5, 6]])
assert not sat([[1, 2, 3], [4, 5], [0, 6]])
assert not sat([[1, 2, 3], [4, 5], [6, 0]])
assert not sat([[1, 2, 3], [4, 5], [6, 0], [7]])
assert not sat([[1, 2, 3], [4, 5, 6], [0]])
assert not sat([[1, 2, 3], [4, 5, 6], [7, 0]])
assert not sat([[1, 2, 3], [4, 5, 6], [7, 8]])
assert not sat([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
assert not sat([[1, 2,

if __name__ == "__main__":
    assert sat(sol())
