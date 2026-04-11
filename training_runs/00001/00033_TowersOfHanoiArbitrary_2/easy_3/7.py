def sat(moves: List[List[int]], source=[[0, 1, 2], [3], [4, 5, 6]], target=[[1, 2, 3], [4, 5], [0, 6]]):
    state = [s[:] for s in source]
    for move in moves:
        i, j = move[0], move[1]
        state[i].insert(j, state[j].pop(0))
    return state == target

def sol():
    return [[1, 2, 3], [4, 5], [0, 6]]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
