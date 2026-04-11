def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 1, 2, 3, 8], [4, 5], [6, 7]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

assert sat([])
assert sat([[0, 7], [4, 5, 6], [1, 2, 3, 8]], [[0, 1, 2, 3, 8], [4, 5], [6, 7]])
assert not sat([[0, 7], [4, 5, 6], [1, 2, 3, 8]], [[0, 1, 2, 3, 8], [4, 5], [7, 6]])
assert not sat([[0, 7], [4, 5, 6], [1, 2, 3, 8]], [[0, 1, 2, 3, 8], [4, 5, 6], [7]])
assert sat([[0, 7], [4, 5, 6], [1, 2, 3, 8]], [[0, 1, 2, 3, 8], [4, 5, 6, 7], []

if __name__ == "__main__":
    assert sat(sol())
