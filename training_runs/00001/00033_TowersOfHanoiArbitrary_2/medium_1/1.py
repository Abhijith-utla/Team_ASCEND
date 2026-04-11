def sat(moves: List[List[int]], source=[[0, 1, 2], [3], [4, 5, 6]], target=[[1, 2, 3], [4, 5], [0, 6]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[i].append(state[j].pop())
        assert state[i] == sorted(state[i])

    return state == target

def sol():
    return []

assert sat([])
assert not sat([[0, 1, 2], [3], [4, 5, 6]])
assert not sat([[0, 1, 2], [3], [4, 5, 7]])
assert sat([[0, 1, 2], [3], [4, 5, 6]], source=[[1, 2, 3], [4, 5], [0, 6]], target=[[1, 2, 3], [4, 5], [0, 6]])
assert not sat([[0, 1, 2], [3], [4, 5, 6]], source=[[1, 2, 3], [4, 5], [0, 6, 7]], target=[[1, 2, 3], [4, 5], [0, 6]])

if __name__ == "__main__":
    assert sat(sol())
