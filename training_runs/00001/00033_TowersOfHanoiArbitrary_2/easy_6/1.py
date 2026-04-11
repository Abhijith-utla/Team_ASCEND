def sat(moves: List[List[int]], source=[[0, 1, 2, 7, 8], [3], [4, 5, 6]], target=[[1, 2, 3, 8], [4, 5], [0, 6]]):
    state = [s[:] for s in source]
    for move in moves:
        state[move[1]].append(state[move[0]].pop())
        if state[move[1]] != sorted(state[move[1]]):
            return False

    return state == target

def sol():
    return []

assert sat([])
assert not sat([[0, 1, 2, 7, 8], [3], [4, 5, 6]])
assert not sat([[0, 1, 2, 7, 8], [3], [4, 5, 6]], [[0, 1, 2, 7, 8], [3], [4, 5, 6]], [[0, 1, 2, 7, 8], [3], [4, 5, 6]])
assert sat([[0, 1, 2, 7, 8], [3], [4, 5, 6]], [[0, 1, 2, 7, 8], [3], [4, 5, 6]], [[1, 2, 3, 8], [4, 5], [0, 6]])
assert not sat([[0, 1, 2, 7, 8], [3], [4, 5, 6]], [[0

if __name__ == "__main__":
    assert sat(sol())
