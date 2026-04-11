def sat(moves: List[List[int]], source=[[0, 1, 2, 3], [4], [5, 6, 7, 8, 9]], target=[[1, 2, 3, 8, 9], [4], [5]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[i].append(state[j].pop())
        assert state[i] == sorted(state[i])

    return state == target

def sol():
    return []

# Test cases
assert sat([[2, 1, 3], [0], [4, 5, 6, 7]])
assert not sat([[2, 1, 3], [0], [4, 5, 6, 7]])
assert sat([[2, 1, 3, 8, 7], [0], [4, 5]])
assert not sat([[2, 1, 3, 8, 7], [0], [4, 5]])

def sol():
    return []

# Test cases
assert sat([[2, 1, 3, 6, 5], [0], [4, 7]])
assert not sat([[2, 1, 3, 6, 5], [0], [4, 7]])
assert sat([[2, 1, 3, 6, 5, 8, 7], [0], [4]])
assert not sat([[2, 1, 3, 6, 5,

if __name__ == "__main__":
    assert sat(sol())
