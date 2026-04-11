def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move[0], move[1]
        state[i].append(state[j].pop(0))
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

# This test case will fail the checker as the source and target states do not match.
assert not sat([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])

# This test case will pass the checker.
assert sat([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])

# This test case will fail the checker as the source and target states do not match.
assert not sat([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]], [[0, 1, 2, 3], [4,

if __name__ == "__main__":
    assert sat(sol())
