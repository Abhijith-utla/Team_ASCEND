def sat(moves: List[List[int]], source=[[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13, 15]], target=[[4, 9, 13, 15], [0, 1, 6, 8, 10, 11, 12, 13]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move
        state[j].insert(0, state[i].pop(0))
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    moves = [[2, 11], [2, 12], [1, 3], [1, 4], [1, 6], [1, 8], [1, 9], [1, 10], [1, 13], [1, 15], [0, 2], [0, 3], [0, 6], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 15]]
    source = [[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13, 15]]
    target = [[4, 9, 13, 15], [0, 1, 6, 8, 10, 11, 12, 13]]

    return sat(moves, source, target)

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
