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

assert sat([])
assert not sat([[0, 0]])
assert not sat([[0, 1]])
assert not sat([[1, 0]])
assert not sat([[1, 1]])
assert not sat([[2, 2]])
assert not sat([[3, 3]])
assert not sat([[4, 4]])
assert not sat([[0, 4]])
assert not sat([[4, 0]])
assert not sat([[5, 5]])
assert not sat([[6, 6]])
assert not sat([[7, 7]])
assert not sat([[4, 5]])
assert not sat([[5, 4]])
assert not sat([[6, 5]])
assert not sat([[5, 6]])
assert not sat([[7, 4]])
assert not sat([[4, 7]])
assert not sat([[7, 0]])
assert not sat([[

if __name__ == "__main__":
    assert sat(sol())
