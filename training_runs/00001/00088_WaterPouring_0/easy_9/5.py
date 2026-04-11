def sat(moves, capacities=[3, 5, 8], init=[8, 0, 0], goal=[4, 4, 0]):
    assert len(moves) > 0, "At least one move must be provided"
    state = init.copy()

    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"
        assert move[0] != move[1], "Cannot pour from same state to itself"
        n = min(capacities[move[1]], state[move[0]] + state[move[1]])
        state[move[0]], state[move[1]] = state[move[0]] + state[move[1]] - n, n

    return state == goal

def sol():
    return [3, 5, 8], [3, 5, 8], [8, 0, 0], [4, 4, 0]

if __name__ == "__main__":
    assert sat(sol())
