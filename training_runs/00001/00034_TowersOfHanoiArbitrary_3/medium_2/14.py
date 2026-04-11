def sat(moves: List[List[int]], source=[[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]], target=[[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move
        state[j].insert(0, state[i].pop(0))
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

assert sat([])
assert not sat([[1, 0]])
assert not sat([[0, 1]])
assert not sat([[0, 0]])
assert not sat([[1, 1]])
assert not sat([[0, 0], [1, 1]])
assert not sat([[1, 1], [0, 0]])
assert not sat([[0, 0], [0, 0]])
assert not sat([[0, 1], [1, 0]])
assert not sat([[0, 1], [0, 1]])
assert not sat([[0, 1], [1, 0], [1, 1]])
assert not sat([[0, 1], [1, 0], [0, 1], [1, 1]])
assert not sat([[0, 1], [1, 0], [0, 1]])
assert not sat([[0, 1], [1, 0], [1, 1], [0,

if __name__ == "__main__":
    assert sat(sol())
