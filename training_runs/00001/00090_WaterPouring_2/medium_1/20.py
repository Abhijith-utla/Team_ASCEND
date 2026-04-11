def sat(moves: List[List[int]], capacities=[357, 298, 492], init=[8, 284, 72], goal=[0, 0, 364]):
    state = init.copy()

    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"
        assert move[0] != move[1], "Cannot pour from same state to itself"
        n = min(capacities[move[1]], state[move[0]] + state[move[1]])
        state[move[0]], state[move[1]] = state[move[0]], n

    return state == goal

def sol():
    return [8, 284, 72]

print(sat([[2, 1], [1, 0], [0, 2]]))
print(sat([[1, 2], [0, 1], [2, 0]]))
print(sat([[2, 1], [1, 0], [0, 2]], capacities=[357, 298, 492], init=[8, 284, 72], goal=[0, 0, 364]))
print(sat([[2, 1], [1, 0], [0, 2]], capacities=[1, 1, 1], init=[8, 0, 0], goal=[0, 0, 364]))
print(sat([[2, 1], [1, 0], [0, 2]], capacities=[357, 298, 492], init=[8, 284, 72], goal=[3

if __name__ == "__main__":
    assert sat(sol())
