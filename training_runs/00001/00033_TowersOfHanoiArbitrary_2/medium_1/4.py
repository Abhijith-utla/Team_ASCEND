def sat(moves: List[List[int]], source=[[0, 1, 2], [3], [4, 5, 6]], target=[[1, 2, 3], [4, 5], [0, 6]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[i].append(state[j].pop())
        assert state[i] == sorted(state[i])

    return state == target

def sol():
    return [[2, 1, 0, 3, 4, 5, 6], [3, 2, 1], [4, 5, 0, 2, 6, 3]]

assert sat(
    moves=[[0, 1], [2, 1], [3, 2], [3, 0], [1, 2], [2, 0]],
    source=[[0, 1, 2], [3], [4, 5, 6]],
    target=[[1, 2, 3], [4, 5], [0, 6]]
)

if __name__ == "__main__":
    assert sat(sol())
