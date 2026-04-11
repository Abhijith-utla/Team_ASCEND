def sat(moves: List[List[int]], source=[[0, 1, 2, 7, 8], [3], [4, 5, 6]], target=[[1, 2, 3, 8], [4, 5], [0, 6]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    moves = [[0, 1], [1, 2], [2, 3], [3, 1]]
    source = [[0, 1, 2, 7, 8], [3], [4, 5, 6]]
    target = [[1, 2, 3, 8], [4, 5], [0, 6]]

    if sat(moves, source, target):
        return "Valid"
    else:
        return "Invalid"

print(sol())

if __name__ == "__main__":
    assert sat(sol())
