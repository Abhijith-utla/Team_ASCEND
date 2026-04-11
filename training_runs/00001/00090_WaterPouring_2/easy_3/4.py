def sat(moves: List[List[int]], capacities=[357, 298, 492], init=[8, 284, 72], goal=[8, 284, 0]):
    state = init.copy()

    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"
        assert move[0] != move[1], "Cannot pour from same state to itself"
        n = min(capacities[move[1]], state[move[0]] + state[move[1]])
        state[move[0]], state[move[1]] = state[move[0]], n

    return state == goal

def sol():
    return [8, 284, 72]

assert sat([])
assert not sat([[1, 2, 2], [2, 1, 1], [2, 1, 0]])
assert not sat([[0, 3, 0], [0, 2, 0], [1, 2, 1]])
assert sat([[2, 0, 0], [1, 1, 1], [2, 1, 0]])
assert not sat([[0, 3, 3], [0, 2, 1], [1, 2, 2]])
assert sat([[3, 0, 3], [2, 1, 2], [2, 0, 0]])
assert not sat([[1, 1, 1], [2, 0, 0], [2, 1, 1]])

if __name__ == "__main__":
    assert sat(sol())
