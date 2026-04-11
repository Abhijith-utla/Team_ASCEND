def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

# Test the function
assert sat([])
assert not sat([[1, 2, 3]])
assert sat([[1, 2], [3, 0], [4]])
assert not sat([[2, 3, 4, 6], [0, 1], [5]])
assert sat([[5, 6], [1, 2, 4], [0, 3]], [[1, 2, 4], [5, 6], [0, 3]], [[2, 3, 4, 6], [0, 1], [5]])
assert not sat([[5, 6], [1, 2, 4], [0, 3]], [[1, 2, 4], [5, 6], [0, 3]], [[2, 3, 4, 5], [0, 1], [6]])
assert not sat([[5, 6], [1, 2, 4], [0, 3]], [[1, 2,

if __name__ == "__main__":
    assert sat(sol())
