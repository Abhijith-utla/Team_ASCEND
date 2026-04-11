def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move[0], move[1]
        state[j].insert(0, state[i].pop(0))  # use pop(0) to change the order of the elements
        assert sorted(state[j]) == state[j]

    return state == target

def sol():
    moves = [[1, 3], [2, 8], [0, 4], [0, 4], [2, 7], [1, 2], [0, 3], [1, 1], [2, 6], [2, 6], [0, 2], [1, 0], [1, 0], [2, 5], [2, 5]]
    source = [[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]]
    target = [[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]

    return sat(moves, source, target)

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
