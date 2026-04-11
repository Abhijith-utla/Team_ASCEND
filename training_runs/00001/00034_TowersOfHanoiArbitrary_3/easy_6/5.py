def sat(moves: List[List[int]], source=[[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13, 15]], target=[[4, 9, 13, 15], [0, 1, 6, 8, 10, 11, 12, 13]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move
        state[j].insert(0, state[i].pop(0))
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

# Checker for solution
def sat(moves: List[List[int]], source=[[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13, 15]], target=[[4, 9, 13, 15], [0, 1, 6, 8, 10, 11, 12, 13]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move
        state[j].insert(0, state[i].pop(0))
        assert state[j] == sorted(state[j])

    return state == target

if __name__ == "__main__":
    assert sat(sol())
