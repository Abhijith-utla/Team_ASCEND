def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], [[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]

# Test cases
def test_case_1():
    moves = [[0, 4], [1, 3]]
    assert sol(moves) == [[1, 3, 5], [0, 4, 2, 8, 14], [7, 6, 9, 10, 11, 12, 13]]

def test_case_2():
    moves = [[1, 1], [0, 3]]
    assert sol(moves) == [[1, 3, 5], [0, 2, 4, 8, 14], [7

if __name__ == "__main__":
    assert sat(sol())
