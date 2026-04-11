def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 7], [1, 2, 3], [4, 5, 6]]):
    state = [s[:] for s in source]

    for i, j in moves:
        state[j].append(state[i].pop())
        assert sorted(state[j]) == target[j]

    return state == target

def sol():
    return [source[:] for source in source]

# Test case
assert sat([[1, 2, 3], [4, 5, 6], [7, 8, 0]], target=[[1, 2, 3], [4, 5, 6], [7, 8, 0]])

# Repeat to check if the function works correctly after multiple moves
assert sat([[1, 2, 3], [4, 5, 6], [7, 8, 0]], target=[[4, 5, 6], [1, 2, 3], [7, 8, 0]])
assert sat([[1, 2, 3], [4, 5, 6], [7, 8, 0]], target=[[4, 5, 6], [1, 2, 3, 7], [8]])
assert sat([[1, 2, 3], [4, 5, 6], [7, 8, 0]], target=[[4,

if __name__ == "__main__":
    assert sat(sol())
