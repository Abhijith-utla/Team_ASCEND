def sat(moves: List[List[int]]):
    state = [0, 1, 2, 3, 4, 5, 6, 7]

    for i, j in moves:
        state[j], state[i] = state[i], state[j]
        assert sorted(state[:j+1]) + state[j+1:] == [0, 1, 2, 3, 4, 5, 6, 7]

    return state == [0, 1, 2, 3, 4, 5, 6, 7]

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
