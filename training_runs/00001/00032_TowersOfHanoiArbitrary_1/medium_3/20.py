def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move[0], move[1]
        state[j].insert(0, state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [[1, 3, 5], [2, 4, 6, 7, 8, 9, 10, 11, 12, 13], [0, 14]]

# The following line will assert that the function sol returns the expected result
assert sat(moves=[[1, 3], [2, 8], [0, 4], [1, 2], [1, 7]])

if __name__ == "__main__":
    assert sat(sol())
