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

# To test the solution
# print(sat([]))  # Expected output: True
# print(sat([[1, 0]]))  # Expected output: True
# print(sat([[1, 2]]))  # Expected output: False
# print(sat([[1, 1], [2, 2], [3, 3]]))  # Expected output: True
# print(sat([[1, 1], [2, 2], [3, 3], [2, 0]]))  # Expected output: False
# print(sat([[2, 0], [1, 1], [3, 2]]))  # Expected output: True

# The first test case is for an empty list of moves. The initial state is [9, 284, 72], and the goal is [0, 0, 364].
# The final state should be [9, 284, 72] for all cases.

# The second

if __name__ == "__main__":
    assert sat(sol())
