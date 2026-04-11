def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

assert sat([])
assert not sat([[1, 2], [0, 3, 4, 5]])
assert not sat([[1, 2], [3, 0, 4, 5]])
assert sat([[1, 2], [3, 4, 0, 5]])
assert not sat([[1, 2, 0], [3, 4, 5]])
assert not sat([[1, 2, 3, 0], [4, 5]])
assert not sat([[1, 2, 3], [4, 5]])
assert sat([[1, 2, 3], [4, 5, 0]])
assert sat([[1, 2, 3, 0], [4, 5, 6]])
assert not sat([[1, 2, 3, 0], [4, 5, 7]])
assert not sat([[1, 2, 3, 0, 6], [4, 5]

if __name__ == "__main__":
    assert sat(sol())
