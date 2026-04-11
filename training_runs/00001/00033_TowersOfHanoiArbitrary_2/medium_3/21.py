def sat(moves: List[List[int]], source=[[0, 1, 2, 3], [4], [5, 6, 7, 8, 9]], target=[[1, 2, 3, 8, 9], [4], [5]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[i].append(state[j].pop())
        assert state[i] == sorted(state[i])

    return state == target

def sol():
    return [[0, 1, 2, 3], [4], [5, 6, 7, 8, 9]]

assert sat(moves=[[0, 1], [1, 2], [2, 0], [0, 3], [3, 0], [0, 2]])
assert not sat(moves=[[0, 1], [1, 2], [2, 0], [0, 3], [3, 0]])
assert sat(moves=[[1, 2], [2, 0], [0, 1], [1, 3], [3, 1], [1, 0]])
assert not sat(moves=[[1, 2], [2, 0], [0, 1], [1, 3], [3, 1]])

if __name__ == "__main__":
    assert sat(sol())
