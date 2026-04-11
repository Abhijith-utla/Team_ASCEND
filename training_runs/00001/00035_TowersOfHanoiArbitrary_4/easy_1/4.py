def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[j].append(state[i].pop(0))
    sorted_state_j = [sorted(state[j]) for j in range(3)]
    sorted_target_j = [sorted(target[j]) for j in range(3)]
    return sorted_state_j == sorted_target_j

def sol():
    return []

# checker should fail without any moves
assert not sat([])

# checker should fail if moves don't form a valid configuration
assert not sat([[0, 1]])
assert not sat([[0, 1], [1, 0]])
assert not sat([[0, 1], [2, 0]])
assert not sat([[0, 1], [1, 2]])
assert not sat([[1, 0]])

# checker should pass if moves form a valid configuration
moves = [[0, 1], [2, 0], [1, 2]]
assert sat(moves)

moves = [[0, 1], [1, 0]]
assert sat(moves)

moves = [[0, 1], [1, 2]]
assert sat(moves)

moves = [[0, 1], [0, 2]]
assert sat(moves)

moves = [[0, 2], [0, 1]]
assert sat(moves)

if __name__ == "__main__":
    assert sat(sol())
