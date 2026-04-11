def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 7], [1, 2, 3], [4, 5, 6]]):
    state = [s[:] for s in source]

    for i, j in moves:
        state[j].append(state[i].pop())
        assert sorted(state[j]) == target[j]

    return state == target

def sol():
    return []

# checker calls
sat([])  # valid
sat([[1, 2, 3]])  # valid
sat([[0, 1, 2]])  # invalid

# examples
assert not sat([[0, 7], [4, 5, 6], [1, 2, 3, 8]], source=[[1, 2, 3], [4, 5, 6], [0, 7]], target=[[1, 2, 3], [0, 4, 5, 6], [7]])
assert not sat([[0, 7], [4, 5, 6], [1, 2, 3, 8]], source=[[1, 2, 3], [4, 5, 6], [0, 7]], target=[[1, 2, 3], [0, 4, 5, 6], [7, 8]])

# more tests
assert sat([[0, 1, 2], [3,

if __name__ == "__main__":
    assert sat(sol())
