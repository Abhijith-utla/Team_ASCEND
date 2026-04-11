def sat(moves: List[List[int]], source=[[0, 1, 6, 7, 8, 9, 14, 16], [5, 15], [2, 3, 4, 10, 11, 12, 13]], target=[[1, 2, 4, 5, 13], [3, 6, 11, 12, 14], [0, 7, 8, 9, 10, 15, 16]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [0, 1, 6, 7, 8, 9, 14, 16, 5, 15, 2, 3, 4, 10, 11, 12, 13]

# The function sat(moves: List[List[int]], source=[[0, 1, 6, 7, 8, 9, 14, 16], [5, 15], [2, 3, 4, 10, 11, 12, 13]], target=[[1, 2, 4, 5, 13], [3, 6, 11, 12, 14], [0, 7, 8, 9, 10, 15, 16]]) checks if the source state and target state are equivalent.
# If they are, it returns True. Otherwise, it returns False.

# The test case:
assert sat([[0, 1, 6, 7, 8,

if __name__ == "__main__":
    assert sat(sol())
