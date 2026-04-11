def sat(moves: List[List[int]], source=[[0, 1, 2, 3], [4], [5, 6, 7, 8, 9]], target=[[1, 2, 3, 8, 9], [4], [5]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move[0], move[1]
        state[i].append(state[j].pop(0))
        assert sorted(state[i]) == state[i]

    return state == target

def sol():
    moves = [
        [0, 1],
        [0, 2],
        [1, 0],
        [1, 2],
        [2, 0],
        [2, 1]
    ]

    source = [[0, 1, 2, 3], [4], [5, 6, 7, 8, 9]]
    target = [[1, 2, 3, 8, 9], [4], [5]]

    assert sat(moves, source, target)

sol()

if __name__ == "__main__":
    assert sat(sol())
