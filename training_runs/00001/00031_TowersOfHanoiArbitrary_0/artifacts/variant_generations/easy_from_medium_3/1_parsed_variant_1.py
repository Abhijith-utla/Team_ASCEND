def sat(moves: List[List[int]], source=[[1, 2, 3, 4], [5, 6, 7, 8]], target=[[2, 1, 4, 3], [7, 5, 8, 6]]):
    state = [s[:] for s in source]

    for i, j in moves:
        state[i].pop(j)
        state[j].insert(0, state[i].pop())
        assert sorted(state[j]) == target[j]

    return state == target

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
