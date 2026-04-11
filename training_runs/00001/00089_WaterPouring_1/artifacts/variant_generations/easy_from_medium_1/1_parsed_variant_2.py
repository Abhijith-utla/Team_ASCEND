def sat(moves, capacities=[724, 43, 611], init=[72, 2, 269], goal=[56, 0, 287]):
    state = init.copy()

    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"
        assert move[0] != move[1], "Cannot pour from same state to itself"
        n = min(capacities[move[1]], state[move[0]] + state[move[1]])
        if n < capacities[move[1]]:
            state[move[0]], state[move[1]] = state[move[0]] + state[move[1]] - n, n
        else:
            state[move[0]], state[move[1]] = state[move[0]] + state[move[1]] - capacities[move[1]], capacities[move[1]]

    return state == goal

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
