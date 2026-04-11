def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

if __name__ == '__main__':
    assert sat([])
    assert sat([[1, 2, 3]])
    assert sat([[1, 2], [0, 3]])
    assert not sat([[1, 3, 2]])
    assert not sat([[2, 1, 3]])
    assert sat([[2, 0, 1, 3], [5, 4]])
    assert not sat([[2, 1, 0, 3], [5, 4]])

if __name__ == '__main__':
    assert sat([[5, 6], [1, 2, 4], [0, 3]], [[2, 3, 4, 6], [0, 1], [5]])
    assert not sat([[5, 6], [1, 2, 4], [0, 3]], [[2, 3, 4, 5], [0, 1], [5]])
    assert not sat

if __name__ == "__main__":
    assert sat(sol())
