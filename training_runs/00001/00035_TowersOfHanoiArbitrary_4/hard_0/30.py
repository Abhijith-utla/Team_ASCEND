def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [5, 6], [1, 2, 4, 0, 3], [[2, 3, 4, 6], [0, 1], [5]]

# Testing the solution
assert sat(moves=[[0, 1]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]])
assert not sat(moves=[[0, 1]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 5], [0, 1], [5]])
assert sat(moves=[[0, 1], [1, 2], [2, 0], [0, 2]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1],

if __name__ == "__main__":
    assert sat(sol())
