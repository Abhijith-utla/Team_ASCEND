def sat(moves: List[List[int]], source=[[0, 1, 2], [3], [4, 5, 6]], target=[[1, 2, 3], [4, 5], [0, 6]]):
    state = [s[:] for s in source]
    for move in moves:
        i, j = move[0], move[1]
        state[i].append(state[j].pop())
        state[i] = sorted(state[i])
    return state == target

def sol():
    return []

assert sat([])
assert not sat([[1, 2, 3], [4, 5], [0, 6]])
assert sat([[1, 2, 3], [4, 5], [0, 6]])
assert not sat([[1, 2, 3], [6, 5], [0, 4]])
assert sat([[1, 2, 3], [6, 5], [0, 4]])
assert not sat([[2, 1, 3], [5, 6], [4, 0]])
assert sat([[2, 1, 3], [5, 6], [4, 0]])
assert not sat([[2, 3, 1], [6, 5], [4, 0]])
assert sat([[2, 3, 1], [6, 5], [4, 0]])
assert not sat([[0, 1, 2], [3], [5, 4, 6]])
assert sat

if __name__ == "__main__":
    assert sat(sol())
