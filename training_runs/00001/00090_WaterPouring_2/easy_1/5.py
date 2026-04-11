def sat(moves: List[List[int]], capacities=[357, 298, 492], init=[50, 299, 72], goal=[0, 0, 364]):
    state = init.copy()

    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"
        assert move[0] != move[1], "Cannot pour from same state to itself"
        n = min(capacities[move[1]], state[move[0]] + state[move[1]])
        state[move[0]], state[move[1]] = state[move[0]], n

    return state == goal

def sol():
    return [50, 299, 72]

assert sat([[4, 1], [3, 2], [1, 0], [2, 0]])
assert not sat([[4, 1], [3, 2], [1, 1], [2, 1]])

if __name__ == "__main__":
    assert sat(sol())
