def sat(moves: List[List[int]]):
    state = [0, 1, 2, 3, 4, 5, 6, 7]

    for i, j in moves:
        state[j], state[i] = state[i], state[j]
        assert sorted(state) == [0, 1, 2, 3, 4, 5, 6, 7]

    return state == [0, 1, 2, 3, 4, 5, 6, 7]

def sol():
    return [0, 1, 2, 3, 4, 5, 6, 7]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
