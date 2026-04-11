def sat(moves: List[List[int]], capacities=[511, 625], init=[472, 153, 127, 500], goal=[97, 625, 30]):
    state = init.copy()

    # Simplifying the moves list
    for move in moves:
        i, j = move
        assert min(i, j) >= 0, "Indices must be non-negative"
        assert i != j, "Cannot pour from same state to itself"
        assert min(i, j) <= capacities[j], "Cannot pour more water than it can hold"
        n = min(capacities[j], state[i] + state[j])
        state[i], state[j] = state[i] + state[j] - n, n

    return state == goal

def sol():
    return [472, 153, 127, 500]

assert sat([[1, 2], [0, 2], [1, 0]])
assert not sat([[1, 2], [1, 0], [0, 0]])
assert not sat([[0, 1], [1, 2], [0, 1]])
assert not sat([[0, 2], [2, 1], [0, 1]])
assert not sat([[0, 2], [2, 0], [1, 1]])
assert not sat([[0, 1], [0, 1], [1, 1]])
assert not sat([[0, 0], [0, 0], [1, 0]])
assert not sat([[0, 1], [1, 1], [0, 0]])
assert not sat([[0, 2], [2, 0], [1, 1]])
assert not sat([[0, 2], [2,

if __name__ == "__main__":
    assert sat(sol())
