def sat(moves: List[List[int]]):
    state = [0, 1, 2, 3, 4, 5, 6, 7]

    for i, j in moves:
        state[i], state[j] = state[j], state[i]
        assert sorted(state) == [0, 1, 2, 3, 4, 5, 6, 7]

    return state == [0, 1, 2, 3, 4, 5, 6, 7]

def sol():
    moves = [
        [0, 1],
        [1, 3],
        [2, 4],
        [3, 7],
        [4, 6],
        [5, 7],
        [6, 5],
        [7, 3]
    ]

    return moves

if __name__ == "__main__":
    assert sat(sol())
