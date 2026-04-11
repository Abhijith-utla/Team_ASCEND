def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move[0], move[1]
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

assert sat(moves=[[1, 2], [2, 0], [0, 1], [2, 3], [3, 2], [2, 4], [4, 0]])
assert not sat(moves=[[1, 2], [2, 0], [0, 1], [2, 3], [3, 2], [2, 4], [4, 0]])

if __name__ == "__main__":
    assert sat(sol())
