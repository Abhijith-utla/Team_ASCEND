def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[6, 7], [0, 1, 2, 3], [4, 5]]):
    state = [s[:] for s in source]
    movements = [state[j].pop(0) for i, j in moves]
    for i, j in moves:
        state[j].append(movements[i])
        assert sorted(state[j]) == target[j]
    return state == target

def sol():
    return []

assert sat([])
assert not sat([[0, 7], [4, 5, 6], [1, 2, 3, 8]])
assert not sat([[0, 7], [4, 5, 6], [1, 2]])
assert not sat([[0, 7], [4, 5, 6]])
assert not sat([[0, 7], [4, 5], [1, 2, 3, 8]])
assert not sat([[0, 7], [4, 5], [1, 2]])
assert not sat([[0, 7], [4, 5]])
assert not sat([[0, 7]])
assert not sat([[4, 5, 6], [1, 2, 3, 8]])
assert not sat([[4, 5, 6], [1, 2]])
assert not sat([[4, 5], [1, 2, 3, 8]])
assert not sat([

if __name__ == "__main__":
    assert sat(sol())
