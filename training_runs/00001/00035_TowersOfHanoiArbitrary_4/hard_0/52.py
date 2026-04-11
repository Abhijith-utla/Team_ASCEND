def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

# If the function is correctly implemented, the assert statement will pass if the code is correct.
assert sat([])
assert not sat([[2, 1, 3], [5, 4]])
assert sat([[2, 1, 3], [5, 4]])
assert not sat([[5, 4], [2, 1, 3]])
assert sat([[5, 4], [2, 3, 1]])
!pip install pytest
assert sat([[5, 1, 2, 4], [3, 0]], [[3, 2, 1, 4, 5], [0, 3]], [[2, 1, 3, 4, 5], [0, 1]])
!pip uninstall pytest
assert not sat([[5, 1, 2, 4], [3, 0]], [[3, 2, 1, 4, 5], [0, 3]], [[2, 1, 3, 4, 5],

if __name__ == "__main__":
    assert sat(sol())
