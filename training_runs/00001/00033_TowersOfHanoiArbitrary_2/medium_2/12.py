def sat(moves: List[List[int]], source=[[0, 1, 2, 7, 8], [3], [4, 5, 6]], target=[[1, 2, 3, 8], [4, 5], [0, 6]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [0, 1, 2, 7, 8, 3, 4, 5, 6]

print(sol())

assert sat(
    moves=[[0, 1], [0, 2], [1, 0], [2, 1], [2, 2], [3, 0], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [5, 3], [5, 4], [6, 1], [6, 2], [6, 3], [6, 4], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4]],
    source=[[0, 1, 2, 7, 8], [3], [4, 5, 6]],
    target=[[1, 2, 3,

if __name__ == "__main__":
    assert sat(sol())
