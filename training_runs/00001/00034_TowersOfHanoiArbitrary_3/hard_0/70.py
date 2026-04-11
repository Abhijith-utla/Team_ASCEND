def sat(moves: List[List[int]], source=[[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]], target=[[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    moves = [[2, 11], [1, 3], [0, 4], [0, 2], [1, 0], [2, 4], [0, 5], [0, 7], [1, 6], [0, 14], [1, 8], [2, 5], [2, 7], [0, 15], [2, 12], [3, 6], [1, 9], [2, 6], [0, 13], [3, 7]]
    source = [[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]]
    target = [[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]]

if __name__ == "__main__":
    assert sat(sol())
