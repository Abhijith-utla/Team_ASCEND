def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move[0], move[1]
        state[i] = state[j]  # replace the whole source state with target state
        assert sorted(state[j]) == state[j]

    return state == target

def sol():
    return [[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]]

def sat(moves: List[List[int]], source=sol(), target=sol()):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move[0], move[1]
        state[i] = state[j]  # replace the whole source state with target state
        assert sorted(state[j]) == state[j]

    return state == target

assert sat([[0, 1], [0, 2], [1, 0], [1, 1]])
assert not sat([[0, 1], [0, 2], [1, 0], [1, 2]])

if __name__ == "__main__":
    assert sat(sol())
