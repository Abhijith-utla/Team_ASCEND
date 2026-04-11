def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 1, 2, 3], [4, 5], [6, 7]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move
        state[j].insert(move[1], state[i].pop(move[0]))
        assert sorted(state[j]) == sorted(target[j])

    return state == target

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
