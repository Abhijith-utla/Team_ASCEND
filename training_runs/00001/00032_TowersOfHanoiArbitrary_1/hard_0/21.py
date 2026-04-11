def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [[1, 3, 5], [2, 6, 7, 8, 9, 10, 11, 12, 13, 14], [0, 4]]

print(sat(moves=[[0, 1], [0, 2], [2, 0], [1, 4], [2, 5], [3, 1], [3, 2], [4, 0], [4, 2], [5, 0], [5, 2], [6, 1], [6, 3], [7, 0], [7, 4], [8, 2], [8, 3], [9, 1], [9, 5], [10, 2], [10, 3], [11, 0], [11, 2], [12, 1], [12, 3], [13, 0], [13, 2], [14, 1], [14, 3]]))

print(sat(

if __name__ == "__main__":
    assert sat(sol())
