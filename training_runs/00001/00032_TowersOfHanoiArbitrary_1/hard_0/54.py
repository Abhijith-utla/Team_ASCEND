def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [sorted(s) for s in [[] for _ in range(14)]]

# test cases

assert sat([[0, 2, 1], [1, 3, 4]])
assert not sat([[0, 3, 2], [1, 4, 3]])
assert sat([[0, 3, 2, 1], [1, 2, 3, 4]])
assert not sat([[0, 3, 1], [2, 1, 3, 4]])
assert sat([[0, 2, 1, 3], [4, 3, 2, 1]])
assert not sat([[0, 3, 1, 2], [3, 2, 1, 4]])
assert sat([[0, 2, 1, 3, 5], [4, 3, 2, 1]])
assert not sat([[0, 3, 1, 2, 4], [5, 4, 2,

if __name__ == "__main__":
    assert sat(sol())
