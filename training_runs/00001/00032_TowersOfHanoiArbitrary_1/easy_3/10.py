def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move[0], move[1]
        state[j] = sorted(state[j])
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

# Test cases
assert sat([[3, 5, 1], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], [[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]], [[5, 12], [0, 3, 4, 6, 7, 9, 10, 11, 12, 13], [1, 2, 8, 14]])
assert not sat([[3, 5, 1], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], [[5, 12], [0, 3, 4, 6, 7, 9, 1

if __name__ == "__main__":
    assert sat(sol())
