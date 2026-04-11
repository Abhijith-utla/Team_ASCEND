def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[6, 7], [0, 1, 2, 3], [4, 5]]):
    state = [s[:] for s in source]

    for i, j in moves:
        state[j].append(state[i].pop())
        assert sorted(state[j]) == target[j]

    return state == target

def sol():
    return []

assert sat([])
assert not sat([[1, 0]])
assert not sat([[0, 1]])
assert not sat([[0, 1], [1, 2], [2, 0]])
assert sat([[1, 0], [2, 3], [0, 2]])
assert not sat([[0, 1], [1, 0]])
assert sat([[0, 2], [2, 1]])
assert not sat([[0, 1], [1, 0], [2, 3]])
assert not sat([[0, 2], [2, 1], [1, 3]])
assert sat([[0, 1], [1, 0], [3, 2]])
assert not sat([[0, 1], [1, 0], [2, 3], [3, 0]])
assert sat([[0, 1, 2], [1, 3, 2], [3, 2, 0]])
assert not

if __name__ == "__main__":
    assert sat(sol())
