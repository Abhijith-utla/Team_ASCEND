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

# Running assertion
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
