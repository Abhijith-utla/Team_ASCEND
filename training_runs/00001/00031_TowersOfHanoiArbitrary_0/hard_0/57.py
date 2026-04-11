def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 1, 2, 3, 8], [4, 5], [6, 7]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    moves = [[0, 7], [4, 5, 6], [1, 2, 3, 8]]
    source = [[0, 7], [4, 5, 6], [1, 2, 3, 8]]
    target = [[0, 1, 2, 3, 8], [4, 5], [6, 7]]

    if sorted(source[0]) != sorted(source[1]) or sorted(source[1]) != sorted(source[2]) or sorted(source[2]) != sorted(source[3]) or sorted(source[3]) != sorted(source[4]) or sorted(source[4]) != sorted(source[5]) or sorted(source[5]) != sorted(source[6]) or sorted(source[6]) != sorted(source[7]):
        return False

    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert sorted(state[

if __name__ == "__main__":
    assert sat(sol())
