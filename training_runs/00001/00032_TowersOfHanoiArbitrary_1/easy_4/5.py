def sat(moves: List[List[int]], source: List[List[int]], target: List[List[int]]):
    state = [s[:] for s in source]
    for move in moves:
        i, j = move[0], move[1]
        state[i].append(state[j].pop(0))
        assert sorted(state[j]) == target[i], 'State not sorted as expected'
    return state == target

def sol():
    return []

# Test
assert sat([[0, 1], [0, 2], [1, 2]], [[2], [1, 0, 1]], [[2], [1, 0, 1]])
assert not sat([[0, 1], [0, 2], [1, 2]], [[2], [1, 0, 1]], [[1, 0], [2]])

if __name__ == "__main__":
    assert sat(sol())
