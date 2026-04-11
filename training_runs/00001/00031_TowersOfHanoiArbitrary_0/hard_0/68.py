def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 1, 2, 3, 8], [4, 5], [6, 7]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

# Test Case 1: [1, 2, 3, 8], [0, 1, 2, 3, 8], [4, 5]
moves = [[1, 2], [2, 3], [3, 0], [0, 1], [1, 0]]
assert sat(moves)

# Test Case 2: [1, 2, 3, 4, 8], [0, 1, 2, 3, 4, 8], [5, 6]
moves = [[1, 2], [2, 3], [3, 4], [4, 0], [0, 1], [1, 0]]
assert not sat(moves)

# Test Case 3: [2, 3, 1, 8], [2, 3, 1, 8], [4, 5]
moves = [[0, 1], [1, 2], [2, 3], [3, 0]]
assert sat(moves

if __name__ == "__main__":
    assert sat(sol())
