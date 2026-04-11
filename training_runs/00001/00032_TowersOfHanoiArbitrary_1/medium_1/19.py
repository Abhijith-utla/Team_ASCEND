def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move[0], move[1]
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    moves = [[1, 3], [2, 8], [0, 4], [0, 6], [0, 7], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13]]
    source = [[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]]
    target = [[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]

    if sat(moves, source, target):
        return moves
    else:
        raise ValueError("Invalid moves")

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
