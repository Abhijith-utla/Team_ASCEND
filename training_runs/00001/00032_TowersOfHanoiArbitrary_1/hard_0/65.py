def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [sorted([1, 3, 5]), sorted([2, 8, 14]), sorted([0, 4, 6, 7, 9, 10, 11, 12, 13])], [sorted([5, 12]), sorted([0, 3, 4, 7, 10, 11]), sorted([1, 2, 6, 8, 9, 13, 14])]

# Checker
def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for

if __name__ == "__main__":
    assert sat(sol())
