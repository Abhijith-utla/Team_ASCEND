def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[6, 7], [0, 1, 2, 3], [4, 5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[j].append(state[i].pop())
        assert sorted(state[j]) == target[j]
    return state == target

def sol():
    return [
        [[6, 7], [0, 1, 2, 3], [4, 5]],
        [[0, 7], [4, 5, 6], [1, 2, 3, 8]],
        [[4, 5], [0, 1, 2, 3], [6, 7]],
        [[1, 2, 3, 8], [0, 7], [4, 5]],
        [[2, 3, 8], [0, 7], [4, 5, 6]],
        [[3, 8], [0, 7], [4, 5, 6]],
        [[8], [0, 7], [4, 5, 6]],
        [[0, 7], [4, 5, 6, 8], [2, 3]],
        [[7], [0, 4, 5, 6, 8], [2, 3]],
        [[6, 8], [0,

if __name__ == "__main__":
    assert sat(sol())
