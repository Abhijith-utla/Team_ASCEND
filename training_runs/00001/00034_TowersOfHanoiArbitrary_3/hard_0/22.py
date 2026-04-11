def sat(moves: List[List[int]], source=[[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]], target=[[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    moves = [[2, 11], [1, 3], [0, 4], [3, 6], [2, 5], [4, 7], [1, 8], [0, 9], [4, 10], [3, 11]]
    source = [[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]]
    target = [[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]]

    if sat(moves, source, target):
        return

# Test cases
assert not sat(moves, source, [x[::-1] for x in target])
assert not sat(moves, source, [x[::-1] for x

if __name__ == "__main__":
    assert sat(sol())
