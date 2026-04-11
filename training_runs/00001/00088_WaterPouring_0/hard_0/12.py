def sat(moves: List[List[int]], capacities=[8, 5, 3], init=[8, 0, 0], goal=[4, 4, 0]):
    state = init.copy()

    for [i, j] in moves:
        assert min(i, j) >= 0, "Indices must be non-negative"
        assert i != j, "Cannot pour from same state to itself"
        n = min(capacities[j], state[i] + state[j])
        state[i], state[j] = state[i] + state[j] - n, n

    return state == goal

def sol():
    return [8, 0, 0]

# Test the solution
assert sat([])
assert not sat([[0, 0]])
assert not sat([[0, 1]])
assert not sat([[0, 2]])
assert not sat([[1, 0]])
assert not sat([[1, 1]])
assert not sat([[1, 2]])
assert not sat([[2, 0]])
assert not sat([[2, 1]])
assert not sat([[2, 2]])
assert not sat([[3, 0]])
assert not sat([[3, 1]])
assert not sat([[3, 2]])
assert not sat([[4, 0]])
assert not sat([[4, 1]])
assert not sat([[4, 2]])
assert not sat([[5, 0]])
assert not sat([[5, 1]])
assert not sat([[5, 2]])
assert not sat([[6, 0]])

if __name__ == "__main__":
    assert sat(sol())
