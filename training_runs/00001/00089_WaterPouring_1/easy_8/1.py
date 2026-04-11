def sat(moves):
    state = [72, 2, 269]
    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"
        assert move[0] != move[1], "Cannot pour from same state to itself"
        n = min(capacities[move[1]], state[move[0]] + state[move[1]])
        state[move[0]], state[move[1]] = state[move[0]] + state[move[1]] - n, n
    return state == goal

def sol():
    return [72, 2, 269]

# We can't run assert statements in the sol function as they need to be in a test case to be run.
# However, we can define a state that satisfies the conditions and return it as the result.

if __name__ == "__main__":
    assert sat(sol())
