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

# assert sat([[3, 0], [0, 3], [2, 0], [1, 1], [0, 1]], capacities=[357, 298, 492], init=[8, 284, 72], goal=[8, 284, 0])
# assert not sat([[2, 1], [1, 2], [2, 0], [1, 1], [0, 1]], capacities=[357, 298, 492], init=[8, 284, 72], goal=[8, 284, 0])
# assert not sat([[3, 0], [0, 3], [2, 0], [1, 1], [2, 2]], capacities=[357, 298, 492], init=[8, 284, 72], goal=[8,

if __name__ == "__main__":
    assert sat(sol())
