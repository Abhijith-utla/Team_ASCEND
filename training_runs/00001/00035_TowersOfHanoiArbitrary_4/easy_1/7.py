def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[j].append(state[i].pop(0))
    sorted_state_j = [sorted(state[j]) for j in range(3)]
    sorted_target_j = [sorted(target[j]) for j in range(3)]
    return sorted_state_j == sorted_target_j

def sol():
    return [[5, 6], [1, 2, 4], [0, 3]], [[2, 3, 4, 6], [0, 1], [5]]

# Test case 1
moves = [[0, 0], [1, 2], [2, 1]]
assert sat(moves)

# Test case 2
moves = [[1, 2], [0, 2], [2, 0]]
assert not sat(moves)

# Test case 3
moves = [[2, 0], [2, 1], [0, 1]]
assert sat(moves)

# Test case 4
moves = [[1, 1], [0, 0], [1, 0]]
assert not sat(moves)

# Test case 5
moves = [[1, 1], [2, 0], [0, 0]]
assert not sat(moves)

if __name__ == "__main__":
    assert sat(sol())
