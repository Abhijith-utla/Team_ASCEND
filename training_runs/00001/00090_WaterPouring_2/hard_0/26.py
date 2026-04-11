def sat(moves: List[List[int]], capacities=[357, 298, 492], init=[8, 284, 72], goal=[0, 0, 364]):
    state = init.copy()

    for [i, j] in moves:
        assert min(i, j) >= 0, "Indices must be non-negative"
        assert i != j, "Cannot pour from same state to itself"
        n = min(capacities[j], state[i] + state[j])
        state[i], state[j] = state[i] + state[j] - n, n

    return state == goal

def sol():
    return [0, 0, 364]

# Test cases
def test_sol():
    assert sol() == [0, 0, 364]
    assert not sat([[1, 0]])
    assert not sat([[0, 1]])
    assert not sat([[0, 0]])
    assert sat([[1, 1]])
    assert sat([[2, 2]])
    assert not sat([[3, 3]])
    assert sat([[0, 3]])
    assert not sat([[2, 0]])
    assert not sat([[0, 2]])
    assert not sat([[1, 2]])
    assert not sat([[0, 1]])
    assert sat([[1, 0], [1, 1]])
    assert not sat([[0, 0]])
    assert not sat([[2, 3]])
    assert sat([[0, 2], [1, 0]])
    assert not sat([[0,

if __name__ == "__main__":
    assert sat(sol())
