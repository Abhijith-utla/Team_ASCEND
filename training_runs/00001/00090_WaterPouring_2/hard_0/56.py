def sat(moves: List[List[int]], capacities=[357, 298, 492], init=[8, 284, 72], goal=[0, 0, 364]):
    state = init.copy()

    for [i, j] in moves:
        assert min(i, j) >= 0, "Indices must be non-negative"
        assert i != j, "Cannot pour from same state to itself"
        n = min(capacities[j], state[i] + state[j])
        state[i], state[j] = state[i] + state[j] - n, n

    return state == goal

def sol():
    return [8, 284, 72]

print(sat([[0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1]]))
print(sat([[0, 0], [0, 1], [1, 0], [1, 2], [2, 0], [2, 1]]))
print(sat([[0, 1], [0, 2], [1, 0], [1, 2], [2, 0]]))
print(sat([[0, 0], [0, 2], [1, 0], [1, 2], [2, 0]]))
print(sat([[0, 0], [0, 1], [1, 0], [1, 2]]))

if __name__ == "__main__":
    assert sat(sol())
