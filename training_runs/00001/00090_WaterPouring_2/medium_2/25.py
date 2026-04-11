def sat(moves: List[List[int]], capacities=[357, 298, 492], init=[9, 284, 72], goal=[0, 0, 364]):
    state = init.copy()

    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"
        assert move[0] != move[1], "Cannot pour from same state to itself"
        n = min(capacities[move[1]], state[move[0]] + state[move[1]])
        state[move[0]], state[move[1]] = state[move[0]], n

    return state == goal

def sol():
    return []

if __name__ == "__main__":
    assert sat([])

# Test case 1: [0, 0, 357], [0, 1, 298], [1, 0, 492], [0, 2, 72], [2, 1, 0]
# Expected output: [0, 0, 364]

# Test case 2: [0, 0, 357], [0, 1, 298], [1, 0, 492], [0, 2, 72], [1, 1, 0]
# Expected output: [0, 1, 357]

# Test case 3: [0, 0, 357], [0, 1, 298], [1, 0, 492], [0, 2, 72], [2, 2, 0]
# Expected output: [0, 1, 356

if __name__ == "__main__":
    assert sat(sol())
