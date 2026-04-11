def sat(moves: List[List[int]], source=[[0, 1, 2, 7, 8], [3], [4, 5, 6]], target=[[1, 2, 3, 8], [4, 5], [0, 6]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

# test case 1
moves1 = [[0, 1], [3, 2], [2, 1]]
source1 = [[0, 1, 2, 7, 8], [3], [4, 5, 6]]
target1 = [[1, 2, 3, 7, 8], [3], [4, 5, 6]]
assert sat(moves1, source1, target1)

# test case 2
moves2 = [[0, 1], [2, 0], [3, 2]]
source2 = [[0, 1, 2, 7, 8], [3], [4, 5, 6]]
target2 = [[1, 2, 3, 7, 8], [4, 5], [0, 6]]
assert sat(moves2, source2, target2)

# test case 3
moves3 = [[1, 0], [2, 0], [3, 2]]
source3 = [[0,

if __name__ == "__main__":
    assert sat(sol())
