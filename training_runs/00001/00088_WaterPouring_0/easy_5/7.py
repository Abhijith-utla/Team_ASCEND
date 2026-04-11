def sat(moves, capacities=[5, 8, 3], init=[3, 0, 0], goal=[4, 4, 0]):
    state = init.copy()

    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"
        assert move[0] != move[1], "Cannot pour from same state to itself"
        n = min(capacities[move[1]], state[move[0]] + state[move[1]])
        state[move[0]], state[move[1]] = state[move[0]] + state[move[1]] - n, n

    return state == goal

def sol():
    return [3, 0, 0]

assert sat([])
assert not sat([[0, 0, 0]])
assert not sat([[1, 0, 1]])
assert not sat([[1, 1, 0]])
assert not sat([[2, 0, 0]])
assert not sat([[3, 0, 0]])
assert sat([[0, 0, 3]])
assert sat([[0, 1, 2]])
assert sat([[1, 1, 1]])
assert sat([[2, 2, 1]])
assert sat([[3, 3, 1]])
assert not sat([[0, 1, 3]])
assert not sat([[1, 2, 2]])
assert not sat([[2, 3, 1]])
assert not sat([[3, 4, 1]])

if __name__ == "__main__":
    assert sat(sol())
