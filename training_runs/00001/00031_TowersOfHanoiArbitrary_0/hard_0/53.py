def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 1, 2, 3, 8], [4, 5], [6, 7]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [0, 7, 4, 5, 6, 1, 2, 3, 8]

# check the solution
assert sat([])
assert not sat([[0, 1]])
assert not sat([[0, 1], [1, 2]])
assert sat([[0, 1], [2, 3]])
assert not sat([[0, 1], [2, 3], [3, 4]])
assert sat([[0, 1], [2, 3], [3, 4], [4, 5]])
assert not sat([[0, 1], [2, 3], [3, 4], [4, 5], [5, 6]])
assert sat([[0, 1], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])

if __name__ == "__main__":
    assert sat(sol())
