def sat(moves: List[List[int]], capacities=[357, 298, 492], init=[9, 284, 72], goal=[50, 0, 364]):
    state = init.copy()

    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"
        assert move[0] != move[1], "Cannot pour from same state to itself"
        n = min(capacities[move[1]], state[move[0]] + state[move[1]])
        state[move[0]], state[move[1]] = n, state[move[1]]

    return state == goal

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
