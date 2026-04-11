def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move[0], move[1]
        state[i].append(state[j].pop(0))
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [[1, 3, 5], [2, 6, 8, 9, 10, 11, 12, 13, 7], [0, 4, 14]]

# test case
print(sat([[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14]]))

if __name__ == "__main__":
    assert sat(sol())
