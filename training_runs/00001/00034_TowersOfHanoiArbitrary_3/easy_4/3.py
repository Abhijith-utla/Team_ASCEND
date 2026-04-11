def sat(moves: List[List[int]], source=[[2, 11, 12], [1, 3, 6, 8, 9]], target=[[0, 2, 3, 11], [9, 1, 6]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move
        state[j].insert(0, state[i].pop(0))
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [[2, 11, 12], [1, 3, 6, 8, 9]]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
