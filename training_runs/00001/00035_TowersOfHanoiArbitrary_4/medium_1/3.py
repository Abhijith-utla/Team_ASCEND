def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[j].append(state[i].pop(0))
        assert sorted(state[j]) == target[j], f'{state[j]} is not equal to {target[j]}'

    return state == target

def sol():
    return []

assert sat([])
assert sat([[1, 2, 3]])
assert not sat([[1, 2, 3], [4, 5, 6]])
assert not sat([[1, 2, 3]])
assert sat([[1, 2, 3], [4, 5, 6]])
assert not sat([[1, 2, 3], [0, 4, 5, 6]])
assert sat([[1, 2, 3], [0, 4, 5, 6]])
assert not sat([[1, 2, 3], [4, 5, 0, 6]])
assert not sat([[1, 2, 3], [4, 5, 6], [0]])
assert sat([[1, 2, 3], [4, 5, 6], [0]])
assert not sat([[1, 2, 3], [4, 0, 5, 6]])
assert not sat([[

if __name__ == "__main__":
    assert sat(sol())
