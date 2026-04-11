def sat(moves: List[List[int]], capacities=[724, 43, 611], init=[72, 2, 269], goal=[56, 0, 287]):
    state = init.copy()

    for [i, j] in moves:
        assert min(i, j) >= 0, "Indices must be non-negative"
        assert i != j, "Cannot pour from same state to itself"
        n = min(capacities[j], state[i] + state[j])
        state[i], state[j] = state[i] + state[j] - n, n

    return state == goal

def sol():
    return [724, 43, 611], [72, 2, 269], [56, 0, 287]

# Correct pattern:
# def sol():
#     return [724, 43, 611], [72, 2, 269], [56, 0, 287]

# Incorrect pattern:
# def sol(x):
#     ...

# assert sat(sol())
# assert not sat(sol([0, 0, 0]))
# assert not sat(sol([611, 43, 724]))
# assert not sat(sol([56, 2, 269]))
# assert not sat(sol([72, 56, 287]))
# assert not sat(sol([724, 611, 269]))

if __name__ == "__main__":
    assert sat(sol())
