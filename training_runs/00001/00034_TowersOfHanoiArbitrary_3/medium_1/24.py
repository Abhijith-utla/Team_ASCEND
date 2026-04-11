def sat(moves: List[List[int]], source=[[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]], target=[[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move
        state[j].append(state[i].pop(0))
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

assert sat([])
assert sat([[1, 2]])
assert sat([[1, 2], [3, 4]])
assert sat([[2, 1], [3, 4], [5, 6]])
assert sat([[3, 1], [2, 4], [5, 6]])
assert sat([[2, 1], [3, 4], [5, 6], [7, 8]])
assert sat([[2, 1, 3], [4, 5, 6], [7, 8]])
assert not sat([[1, 2], [3, 4], [5, 6]])
assert not sat([[1, 2, 3], [4, 5, 6, 7], [8, 9]])
assert not sat([[1, 2, 3], [5, 6, 7], [8, 9, 4]])
assert not sat([[1, 2, 3], [5, 6,

if __name__ == "__main__":
    assert sat(sol())
