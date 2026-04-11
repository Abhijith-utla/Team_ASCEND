def sat(moves, capacities=[5, 8, 3], init=[8, 0, 0], goal=[4, 4, 0]):
    state = init.copy()

    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"
        assert move[0] != move[1], "Cannot pour from same state to itself"
        n = min(capacities[move[1]], state[move[0]] + state[move[1]])
        state[move[0]], state[move[1]] = state[move[0]] + state[move[1]] - n, n

    return state == goal

def sol():
    return [8, 0, 0]

# Uncomment this if you want to test your function
# assert sat([])
# assert not sat([[0, 1, 0], [1, 0, 0], [2, 0, 0]])
# assert not sat([[0, 1, 0], [0, 0, 0], [2, 0, 0]])
# assert not sat([[0, 1, 0], [1, 0, 1], [2, 0, 0]])
# assert not sat([[0, 0, 0], [1, 0, 0], [2, 0, 0]])
# assert not sat([[0, 0, 0], [1, 0, 0], [1, 1, 0]])
# assert not sat([[0, 0, 0], [0, 1, 1], [2, 0, 0]])
# assert not sat([[0, 0, 0], [0

if __name__ == "__main__":
    assert sat(sol())
