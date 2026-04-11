def sat(moves: List[List[int]], capacities=[511, 625, 553], init=[472, 153, 127], goal=[97, 625, 100]):
    state = init.copy()

    for [i, j] in moves:
        assert min(i, j) >= 0, "Indices must be non-negative"
        assert i != j, "Cannot pour from same state to itself"
        assert min(i, j) <= capacities[j], "Cannot pour more water than it can hold"
        n = min(capacities[j], state[i] + state[j])
        state[i], state[j] = state[i] + state[j] - n, n

    return state == goal

def sol():
    return [472, 153, 127]

assert sat([])
assert not sat([[0, 0, 1]])
assert not sat([[0, 1, 0]])
assert sat([[0, 0, 1], [1, 0, 0], [1, 0, 0]])
assert not sat([[1, 0, 0], [1, 0, 0], [0, 0, 1]])
assert not sat([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
assert not sat([[0, 0, 1], [1, 0, 0], [0, 0, 1]])
assert not sat([[0, 0, 1], [1, 1, 0], [0, 0, 0]])

if __name__ == "__main__":
    assert sat(sol())
