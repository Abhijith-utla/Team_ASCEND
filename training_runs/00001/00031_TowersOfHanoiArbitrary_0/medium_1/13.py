def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 1, 2, 3], [4, 5], [6, 7]]):
    state = [s[:] for s in source]

    for i, j in moves:
        state[j].append(state[i].pop())
        assert sorted(state[j]) == target[j]

    return state == target

def sol():
    return [
        [[], [4, 5, 6, 7], [0, 1, 2, 3]],
        [[1, 0], [4, 5, 6, 7], [0, 2, 3]],
        [[2, 0], [4, 5, 6, 7], [0, 1, 3]],
        [[3, 0], [4, 5, 6, 7], [0, 1, 2]],
        [[1, 1], [4, 5, 6, 7], [0, 2, 3]],
        [[2, 1], [4, 5, 6, 7], [0, 1, 3]],
        [[3, 1], [4, 5, 6, 7], [0, 1, 2]],
        [[0, 2], [4, 5, 6, 7], [1, 3]],
        [[1, 2], [4, 5

if __name__ == "__main__":
    assert sat(sol())
