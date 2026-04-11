def sat(moves: List[List[int]], source=[[0, 1, 2], [3], [4, 5, 6]], target=[[1, 2, 3], [4, 5], [0, 6]]):
    state = [s[:] for s in source]
    for move in moves:
        i, j = move[0], move[1]
        state[i].append(state[j].pop())
        state[i] = sorted(state[i])
    return state == target

def sol():
    return [0, 1, 2, 3, 4, 5, 6]

print(sat([[0, 1, 2], [3], [4, 5, 6]], [[1, 2, 3], [4, 5], [0, 6]], [[1, 2, 3], [4, 5], [0, 6]]))  # True
print(sat([[0, 1, 2], [3], [4, 5, 6]], [[1, 2, 3], [4, 5], [6, 0]], [[1, 2, 3], [4, 5], [0, 6]]))  # False
print(sat([[0, 1, 2], [3], [4, 5, 6]], [[1, 2, 3], [4, 5], [0, 6]], [[1, 2, 3], [4, 5], [0, 6, 7, 8, 9]]))

if __name__ == "__main__":
    assert sat(sol())
