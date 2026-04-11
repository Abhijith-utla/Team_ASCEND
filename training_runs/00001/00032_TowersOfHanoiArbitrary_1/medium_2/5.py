def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move[0], move[1]
        state[i].append(state[j].pop(0))
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

print(sat([]))
print(sat([[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]]))
print(sat([[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]))
print(sat([[1, 3, 5], [0, 4, 6, 7, 8, 9, 10, 11, 12, 13], [2, 14]]))
print(sat([[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]))
print(sat([[5, 12], [0, 3

if __name__ == "__main__":
    assert sat(sol())
