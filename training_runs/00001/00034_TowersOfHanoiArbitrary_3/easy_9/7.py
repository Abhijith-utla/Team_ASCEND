def sat(moves: List[List[int]], source=[[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]], target=[[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move
        state[i].insert(0, state[j].pop(0))
        assert sorted(state[i]) == sorted(state[i])

    return sorted(state) == sorted(target)

def sol():
    return [
        [[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]],
        [[1, 3, 6, 8, 9, 10, 13], [0, 2, 5, 7, 14, 15], [2, 11, 12, 16]],
        [[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]],
        [[0, 2, 3, 5, 7, 8, 14, 16], [1, 6], [9, 11, 12, 13, 15]],
        [[0, 4, 5,

if __name__ == "__main__":
    assert sat(sol())
