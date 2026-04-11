def sat(moves: List[List[int]], capacities=[511, 625, 553], init=[472, 153, 127], goal=[97, 625, 30]):
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

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
