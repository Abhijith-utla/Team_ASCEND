def sat(moves: List[List[int]], capacities=[357, 298, 492], init=[8, 284, 70], goal=[98, 0, 364]):
    state = init.copy()

    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"
        assert move[0] != move[1], "Cannot pour from same state to itself"
        n = min(capacities[move[1]], state[move[0]] + state[move[1]])
        state[move[0]], state[move[1]] = state[move[0]], n

    return state == goal

def sol():
    return [8, 284, 70]

# Assertion to test the correctness of the solution
assert sat([])

# Assertion to test the correctness of the solution
assert sat([[0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1]])

# Assertion to test the correctness of the solution
assert not sat([[0, 1], [0, 2], [1, 0], [1, 2], [2, 0]])

# Assertion to test the correctness of the solution
assert not sat([[0, 0]])

# Assertion to test the correctness of the solution
assert not sat([[0, 1], [0, 2], [1, 0], [1, 2], [2, 1]])

# Assertion to test the correctness of the solution
assert sat([[1, 2], [2, 1]])

if __name__ == "__main__":
    assert sat(sol())
