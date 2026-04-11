def sat(moves: List[List[int]], source=[[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]], target=[[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move
        state[i], state[j] = state[j], state[i]
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

# test cases
assert sat([[1, 2, 3, 4, 5], [4, 5, 6, 1, 2], [3, 4, 2, 6, 1]])
assert not sat([[1, 2, 3, 4, 5], [4, 5, 6, 2, 1], [3, 4, 2, 6, 1]])
assert sat([[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]],
           [[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]],
           [[0, 2, 3, 5, 7, 8

if __name__ == "__main__":
    assert sat(sol())
