def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

# Checker should not run, but this function is necessary for the test to work
assert sat([])

# Checker should pass
assert sat([[2, 3, 4, 6], [0, 1], [5]])

# Checker should pass
assert not sat([[2, 3, 4, 6], [0, 1, 5], [5]])

# Checker should pass
assert sat([[1, 2, 3, 4, 5], [0], [6]])

# Checker should fail
assert not sat([[2, 3, 4, 5, 1], [0, 3], [6]])

# Checker should pass
assert sat([[1, 2, 3, 4, 5], [0, 3], [6]])

if __name__ == "__main__":
    assert sat(sol())
