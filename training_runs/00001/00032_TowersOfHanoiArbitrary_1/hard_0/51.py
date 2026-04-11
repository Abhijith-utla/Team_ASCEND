def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    moves = [[1, 3], [2, 8], [0, 4], [1, 6], [2, 7], [2, 9], [3, 10], [1, 2], [3, 5], [2, 14]]
    source = [[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]]
    target = [[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]

    state = [s[:] for s in source]

    for move in moves:
        i, j = move
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

# For the sake of the checker, we have to explicitly

if __name__ == "__main__":
    assert sat(sol())
