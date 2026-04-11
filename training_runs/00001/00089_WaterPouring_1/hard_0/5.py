def sat(moves: List[List[int]], capacities=[724, 43, 611], init=[72, 2, 269], goal=[56, 0, 287]):
    state = init.copy()

    for [i, j] in moves:
        assert min(i, j) >= 0, "Indices must be non-negative"
        assert i != j, "Cannot pour from same state to itself"
        n = min(capacities[j], state[i] + state[j])
        state[i], state[j] = state[i] + state[j] - n, n

    return state == goal

def sol():
    return []

# This test is not valid because we do not know the moves. We can use the `moves` variable to simulate the game until we reach a state that is equal to the goal state.

def test():
    moves = [] # Replace this with the actual moves.
    capacities = [724, 43, 611]
    init = [72, 2, 269]
    goal = [56, 0, 287]
    
    state = init.copy()

    while True:
        assert min(min(state), goal[-1]) >= 0, "Indices must be non-negative"
        assert state != goal, "Cannot pour from same state to itself"
        n = min(capacities[state.index(min(state))], state[state.index(min(state))] + state[state.index(min(state))])
        state[state.index(min(state))], state[state.index(min(state))] = state[state.index(min(state))] +

if __name__ == "__main__":
    assert sat(sol())
