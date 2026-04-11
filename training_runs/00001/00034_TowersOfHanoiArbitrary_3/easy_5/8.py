def sat(moves: List[List[int]], source=[[2, 11, 12, 16], [1, 3, 6, 8, 9, 10]], target=[[1, 3, 6, 10], [2, 11, 16]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move
        state[j].insert(0, state[i].pop(0))
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

# This function is not used, it is an placeholder for the sol function.
# Please write your solution in the sol function below.

if __name__ == "__main__":
    assert sat(sol())
