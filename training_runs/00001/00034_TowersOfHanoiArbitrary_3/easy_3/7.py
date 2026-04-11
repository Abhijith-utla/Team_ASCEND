def sat(moves: List[List[int]], source=[[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]], target=[[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move
        state[i] = state[j]
        state[j] = []
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    moves = [[2, 11], [0, 4], [1, 3], [2, 10], [0, 1], [0, 3], [1, 2], [3, 1], [0, 2], [2, 11]]
    source = [[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]]
    target = [[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]]

    if sat(moves, source, target):
        return "Correct"
    else:
        return "Incorrect"

print(sol())

if __name__ == "__main__":
    assert sat(sol())
