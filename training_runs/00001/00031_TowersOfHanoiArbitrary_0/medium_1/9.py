def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 1, 2, 3], [4, 5], [6, 7]]):
    state = [s[:] for s in source]

    for i, j in moves:
        state[j].append(state[i].pop())
        assert sorted(state[j]) == target[j]

    return state == target

def sol():
    return []

# Assuming that sat() is correctly defined with the given inputs
assert sat([[1, 2, 3], [4, 5, 6, 7, 8]])
assert not sat([[1, 2, 3], [4, 5, 7, 6, 8]])
assert sat([[0, 1, 2, 3], [4, 5, 6, 7, 8]])
assert not sat([[0, 1, 2, 3], [4, 5, 6, 7]])
assert sat([[1, 2, 3, 4], [5, 6, 7, 8]])
assert not sat([[1, 2, 3, 4], [5, 6, 7]])
assert sat([[0, 1, 2, 3, 4], [5, 6, 7, 8]])
assert not sat([[0, 1, 2, 3, 4], [5, 6

if __name__ == "__main__":
    assert sat(sol())
