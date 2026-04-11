def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

# test the function
if __name__ == "__main__":
    assert sat([])
    assert sat([[1, 2, 3]])
    assert not sat([[1, 2], [0, 3, 4, 5]])
    assert sat([[1, 2], [3, 0, 4, 5, 6]])
    assert sat([[1, 2, 3], [4, 5, 0, 6, 7]])
    assert sat([[1, 2, 3], [4, 5, 6, 0, 7]])
    assert not sat([[1, 2, 3], [4, 5, 0, 6, 7, 8]])
    assert sat([[1, 2, 3], [4, 5, 6, 7, 0]])
    assert sat([[1, 2, 3, 4, 5], [6, 7, 8, 0]])

if __name__ == "__main__":
    assert sat(sol())
