def sat(moves: List[List[int]], capacities=[357, 298, 492], init=[9, 284, 72], goal=[0, 0, 364]):
    state = init.copy()

    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"
        assert move[0] != move[1], "Cannot pour from same state to itself"
        n = min(capacities[move[1]], state[move[0]] + state[move[1]])
        state[move[0]], state[move[1]] = n, state[move[1]]

    return state == goal

def sol():
    return [9, 284, 72]

assert sat([])
assert not sat([[0, 1, 3], [0, 1, 2], [0, 2, 2], [1, 1, 2], [1, 2, 0], [2, 0, 2]])
assert not sat([[0, 1, 2], [0, 2, 2], [0, 2, 1], [1, 0, 1], [1, 2, 0], [2, 1, 1]])
assert sat([[0, 0, 357], [0, 1, 298], [0, 2, 492], [1, 1, 9], [1, 2, 284], [2, 0, 72], [2, 2, 364]])
assert not sat([[0, 0, 357], [0, 1, 298], [0, 2

if __name__ == "__main__":
    assert sat(sol())
