def sat(moves: List[List[int]], source=[[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]], target=[[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    moves = [[2, 11], [0, 2], [1, 0], [3, 1], [2, 3], [0, 3], [0, 1], [1, 2], [3, 0], [0, 4], [2, 0], [1, 3], [0, 2], [3, 2], [2, 4], [0, 5], [1, 1], [4, 3], [3, 1], [2, 5], [1, 4], [0, 0], [4, 1], [3, 0], [1, 3], [2, 2], [4, 0]]
    source = [[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]]
    target = [[0, 2, 3, 5, 7, 8, 1

if __name__ == "__main__":
    assert sat(sol())
