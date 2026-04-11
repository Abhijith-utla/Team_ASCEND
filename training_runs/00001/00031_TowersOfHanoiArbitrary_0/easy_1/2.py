def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 1, 2, 3], [4, 5], [6, 7]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move
        state[j].append(state[i].pop(move[0]))
        assert sorted(state[j]) == sorted(target[j])

    return state == target

def sol():
    return []

# Test case 1
moves = [[0, 7], [4, 5, 6], [1, 2, 3, 8]]
assert sol(moves) == [[0, 7], [4, 5, 6], [1, 2, 3, 8]]

# Test case 2
moves = [[1, 2], [3, 0, 4], [5, 6]]
assert sol(moves) == [[1, 2], [3, 5, 4], [0, 6]]

# Test case 3
moves = [[2, 0], [1, 3, 4], [5, 6, 7]]
assert sol(moves) == [[2, 0], [1, 5, 4], [3, 6, 7]]

# Test case 4
moves = [[1, 3], [0, 4, 2], [5, 7, 6]]
assert sol(moves) == [[1, 3

if __name__ == "__main__":
    assert sat(sol())
