def sat(moves: List[List[int]]):
    state = [0, 1, 2, 3, 4, 5, 6, 7]

    for i, j in moves:
        state[i], state[j] = state[j], state[i]
        assert sorted(state) == [0, 1, 2, 3, 4, 5, 6, 7]

    return state == [0, 1, 2, 3, 4, 5, 6, 7]

def sol():
    return [0, 1, 2, 3, 4, 5, 6, 7]

if __name__ == "__main__":
    assert sat(sol())
