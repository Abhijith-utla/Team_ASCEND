def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move[0], move[1]
        state[j].insert(0, state[i].pop())
        assert sorted(state[j]) == state[j]

    return state == target

def sol():
    moves = [
        [0, 4],
        [2, 0],
        [1, 3],
        [1, 0],
        [2, 1],
        [2, 3],
        [0, 2],
        [1, 2],
        [1, 0],
        [2, 0],
        [0, 1],
        [0, 3],
        [2, 2],
        [2, 1],
        [1, 3],
        [0, 0],
        [2, 3],
        [1, 2],
        [2, 0],
        [0, 3],
        [1, 0],
        [0, 2],
        [0, 1],
        [1, 1],
        [1, 3],
        [2, 3],
        [0, 3],
        [1, 2],
        [2, 2],
        [0, 2],
        [2, 1],

if __name__ == "__main__":
    assert sat(sol())
