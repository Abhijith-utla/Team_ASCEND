def sat(moves: List[List[int]], capacities=[511, 625, 553], init=[472, 153, 127], goal=[97, 625, 90]):
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
assert not sat([[0, 0, 472]])
assert not sat([[0, 0, 511]])
assert not sat([[0, 0, 510]])
assert not sat([[0, 0, 511], [0, 0, 625]])
assert not sat([[0, 0, 553]])
assert not sat([[0, 0, 624]])
assert not sat([[0, 511, 0]])
assert not sat([[0, 512, 0]])
assert not sat([[472, 0, 0]])
assert not sat([[473, 0, 0]])
assert not sat([[510, 0, 0]])
assert not sat([[510, 510, 0]])
assert not sat([[510,

if __name__ == "__main__":
    assert sat(sol())
