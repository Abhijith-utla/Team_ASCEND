def sat(moves, capacities=[3, 5, 8], init=[8, 0, 0], goal=[4, 4, 0]):
    state = init.copy()

    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"
        assert move[0] != move[1], "Cannot pour from same state to itself"
        n = min(capacities[move[1]], state[move[0]] + state[move[1]])
        state[move[0]], state[move[1]] = state[move[0]] + state[move[1]] - n, n

    return state == goal

def sol():
    return [8, 0, 0]

# The result should be [4, 4, 0]
print(sat([[1, 0], [6, 5], [3, 3]])) 

# The result should be [8, 1, 0]
print(sat([[2, 0], [6, 4], [3, 2]])) 

# The result should be [6, 1, 0]
print(sat([[1, 1], [6, 5], [3, 3]])) 

# The result should be [0, 1, 0]
print(sat([[2, 1], [6, 4], [3, 2]])) 

# The result should be [0, 2, 0]
print(sat([[2, 2], [6, 4], [3, 2]])) 

# The result should be [0, 3, 0]
print(sat([[3, 2], [6, 4], [3,

if __name__ == "__main__":
    assert sat(sol())
