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

# The function "sol" always returns the state [8, 0, 0] regardless of the input "moves". This is because in the game of pendulum, the goal is to reach the state [4, 4, 0] from the initial state [8, 0, 0]. This state is not achievable by any valid move in the game, so the function "sol" always returns the same state.

if __name__ == "__main__":
    assert sat(sol())
