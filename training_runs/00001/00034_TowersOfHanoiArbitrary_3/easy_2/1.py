def sat(moves: List[List[int]], source=[[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]], target=[[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move
        state[i], state[j] = state[j], state[i]
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [2, 11, 12, 16, 1, 3, 6, 8, 9, 10, 13, 0, 4, 5, 7, 14, 15, 10]

assert sat(moves=[[1, 0], [0, 2], [3, 1]])
assert not sat(moves=[[1, 0], [0, 2], [3, 3]])
assert sat(moves=[[1, 0], [0, 2], [3, 1], [2, 3]])
assert not sat(moves=[[1, 0], [0, 2], [3, 3]])
assert sat(moves=[[0, 3], [1, 2], [2, 0], [3, 1]])
assert not sat(moves=[[0, 3], [1, 2], [2, 0], [4, 1]])

if __name__ == "__main__":
    assert sat(sol())
