def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[i].insert(0, state[j].pop())
    sorted_state_j = [sorted(state[j]) for j in range(3)]
    sorted_target_j = [sorted(target[j]) for j in range(3)]
    return sorted_state_j == sorted_target_j

def sol():
    return []

assert sat([])
assert sat([[1, 2, 3, 4, 5]])
assert sat([[1, 2, 3, 4, 5], [0, 6]])
assert sat([[1, 2, 3, 4, 5], [0, 6], [7]])
assert not sat([[1, 2, 3, 4, 5], [0, 6, 7], [8, 9]])
assert not sat([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 11]])
assert not sat([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1], [12]])
assert not sat([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,

if __name__ == "__main__":
    assert sat(sol())
