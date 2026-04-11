def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[6, 7], [0, 1, 2, 3], [4, 5]]):
    state = [s[:] for s in source]
    movements = [state[j].pop(0) for i, j in moves]
    for i, j in moves:
        state[j].append(movements[i])
        assert sorted(state[j]) == target[j]
    return state == target

def sol():
    return [[5, 6, 7, 0, 1, 2, 3, 4], [6, 7, 0, 1, 2, 3, 4, 5]]

print(sat([[0, 7], [4, 5, 6], [1, 2, 3, 8]]))
print(sat([[1, 2, 3, 8], [4, 5], [0, 7]]))
print(sat([[1, 2, 3, 8], [4, 5], [6, 7]]))
print(sat([[0, 7], [4, 5, 6], [1, 2, 3, 8]]))
print(sat([[1, 2, 3, 8], [4, 5], [0, 7]]))
print(sat([[0, 7], [4, 5, 6], [1, 2, 3, 8]]))
print(sat([[1, 2,

if __name__ == "__main__":
    assert sat(sol())
