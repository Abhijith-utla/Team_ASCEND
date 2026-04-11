def sat(moves: List[List[int]], source=[[0, 1, 6, 7, 8, 9, 14, 16], [5, 15], [2, 3, 4, 10, 11, 12, 13]], target=[[1, 2, 4, 5, 13], [3, 6, 11, 12, 14], [0, 7, 8, 9, 10, 15, 16]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [[0, 1, 6, 7, 8, 9, 14, 16], [5, 15], [2, 3, 4, 10, 11, 12, 13]]

# Test case 1: The first move should switch the numbers 2 and 5, but not 4 and 10
moves = [[1, 0], [2, 1]]
assert sat(moves, source, target)

# Test case 2: The second move should switch the numbers 5 and 15, but not 6 and 11
moves = [[0, 0], [1, 1]]
assert not sat(moves, source, target)

# Test case 3: The third move should switch the numbers 4 and 10, but not 3 and 6
moves = [[0, 1], [2, 0]]
assert not sat(moves, source, target)

# Test case 4: The fourth move should switch the numbers 3, 6 and

if __name__ == "__main__":
    assert sat(sol())
