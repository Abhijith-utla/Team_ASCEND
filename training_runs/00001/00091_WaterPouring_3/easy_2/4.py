def sat(moves: List[List[int]], capacities=[511, 625, 553], init=[472, 153], goal=[97, 625, 30]):
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
    return [472, 153, 0]

assert sat([[0, 1, 511], [2, 1, 625], [3, 2, 553], [0, 0, 97], [1, 0, 625], [2, 1, 30]])

if __name__ == "__main__":
    assert sat(sol())
