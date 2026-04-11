def sat(moves: List[List[int]], capacities=[86, 259, 281], init=[47, 18, 35], goal=[35, 0, 65]):
    state = init.copy()

    for [i, j] in moves:
        assert min(i, j) >= 0, "Indices must be non-negative"
        assert i != j, "Cannot pour from same state to itself"
        n = min(capacities[j], state[i] + state[j])
        state[i], state[j] = state[i] + state[j] - n, n

    return state == goal

def sol(moves: List[List[int]], capacities=[86, 259, 281], init=[47, 18, 35], goal=[35, 0, 65]):
    state = init.copy()

    for [i, j] in moves:
        assert min(i, j) >= 0, "Indices must be non-negative"
        assert i != j, "Cannot pour from same state to itself"
        n = min(capacities[j], state[i] + state[j])
        state[i], state[j] = state[i] + state[j] - n, n

    return state == goal

if __name__ == "__main__":
    assert sat(sol())
