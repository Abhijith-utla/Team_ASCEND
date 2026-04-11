def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

assert sat([])
assert sat([[1, 2, 3]])
assert not sat([[1, 2], [3, 4]])
assert sat([[1, 2], [0, 3]])
assert sat([[1, 2, 3], [0, 4]])
assert not sat([[1, 2, 3], [0, 4, 5, 6]])
assert sat([[1, 2, 3, 4], [0]])
assert not sat([[1, 2, 3], [0, 2]])
assert not sat([[1, 2, 3], [0, 1, 2, 3, 4]])
assert not sat([[1, 2, 3, 4], [0, 1, 2, 3]])
assert sat([[1, 2, 3, 4], [0, 1, 2, 3, 4]])
assert not sat([[1, 2, 3

if __name__ == "__main__":
    assert sat(sol())
