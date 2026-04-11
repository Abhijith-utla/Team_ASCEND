def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 1, 2, 3], [4, 5], [6, 7]]):
    state = [s[:] for s in source]

    for i, j in moves:
        state[j].insert(0, state[i].pop())    # insert() method used instead of append()
        assert sorted(state[j]) == target[j]

    return state == target

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
