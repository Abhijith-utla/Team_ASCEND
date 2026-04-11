def sat(moves: List[List[int]], capacities=[357, 298, 492], init=[8, 284, 72], goal=[0, 0, 364]):
    state = init.copy()

    for [i, j] in moves:
        assert min(i, j) >= 0, "Indices must be non-negative"
        assert i != j, "Cannot pour from same state to itself"
        n = min(capacities[j], state[i] + state[j])
        state[i], state[j] = state[i] + state[j] - n, n

    return state == goal

def sol():
    return [357, 298, 492], [8, 284, 72], [0, 0, 364]

# Checker
assert sat(*sol())

if __name__ == "__main__":
    assert sat(sol())
