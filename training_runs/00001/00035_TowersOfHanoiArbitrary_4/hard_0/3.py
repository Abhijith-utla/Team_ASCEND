def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

assert sat([])
assert not sat([[2, 1, 0]])
assert not sat([[0, 2, 1]])
assert sat([[1, 2, 0]])
assert not sat([[0, 1, 2]])
assert not sat([[0, 1, 2], [1, 2, 0]])
assert sat([[0, 1, 2], [1, 2, 0], [2, 0, 1]])
assert not sat([[0, 1, 2], [1, 0, 2]])
assert not sat([[0, 1, 2], [0, 2, 1]])
assert not sat([[0, 1, 2], [1, 2, 0]])
assert not sat([[0, 2, 1], [1, 2, 0]])
assert not sat([[1, 2, 0], [0, 2, 1]])
assert not sat([[1

if __name__ == "__main__":
    assert sat(sol())
