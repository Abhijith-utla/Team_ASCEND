def sat(moves: List[List[int]], source=[[1, 2, 3, 4], [5, 6, 7, 8]], target=[[2, 1, 3, 4], [7, 5, 6, 8]]):
    state = [s[:] for s in source]

    for i, j in moves:
        state[i].pop(j)
        state[j].insert(0, state[i].pop(0))
        assert sorted(state[j]) == target[j]

    return state == target

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
