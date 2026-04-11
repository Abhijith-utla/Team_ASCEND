def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 1, 2, 3, 8], [4, 5], [6, 7]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [[0, 7], [4, 5, 6], [1, 2, 3, 8]]

# Testing the solution
moves = [[0, 1], [1, 2], [2, 3]]
assert sat(moves)

moves = [[0, 0]]
assert not sat(moves)

moves = [[0, 1], [2, 1], [1, 0]]
assert sat(moves)

moves = [[2, 0]]
assert not sat(moves)

moves = [[0, 1], [1, 2], [1, 0]]
assert sat(moves)

moves = [[2, 0], [1, 1]]
assert not sat(moves)

moves = [[1, 0]]
assert sat(moves)

moves = [[0, 0]]
assert sat(moves)

moves = [[0, 1], [0, 0]]
assert not sat(moves)

m

if __name__ == "__main__":
    assert sat(sol())
