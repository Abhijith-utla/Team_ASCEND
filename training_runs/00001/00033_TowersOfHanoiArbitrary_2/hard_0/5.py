def sat(moves: List[List[int]], source=[[0, 1, 6, 7, 8, 9, 14, 16], [5, 15], [2, 3, 4, 10, 11, 12, 13]], target=[[1, 2, 4, 5, 13], [3, 6, 11, 12, 14], [0, 7, 8, 9, 10, 15, 16]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    moves = [[0, 1], [5, 1], [2, 3], [2, 4], [5, 6], [5, 7], [2, 8], [2, 9], [1, 10], [1, 11], [0, 12], [0, 13], [3, 14], [3, 15], [4, 16]]

    def sat(moves: List[List[int]], source=[[0, 1, 6, 7, 8, 9, 14, 16], [5, 15], [2, 3, 4, 10, 11, 12, 13]], target=[[1, 2, 4, 5, 13], [3, 6, 11, 12, 14], [0, 7, 8, 9, 10, 15, 16]]):
        state = [s[:] for s in source]

if __name__ == "__main__":
    assert sat(sol())
