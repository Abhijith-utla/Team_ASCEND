def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [5, 6], [1, 2, 4], [0, 3]

assert sat([[5, 6], [1, 2, 4], [0, 3]])

moves = [(0, 2), (1, 0), (2, 1)]
for i, j in moves:
    source[j].append(source[i].pop())
    assert source[j] == sorted(source[j])

return source == target

if __name__ == "__main__":
    assert sat(sol())
