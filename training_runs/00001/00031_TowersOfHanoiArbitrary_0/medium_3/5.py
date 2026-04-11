def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 7], [1, 2, 3], [4, 5, 6]]):
    state = [s[:] for s in source]

    for i, j in moves:
        state[j].append(state[i].pop())
        assert sorted(state[j]) == target[j]

    return state == target

def sol():
    return [source[:] for source in [source[:] for source in source]]

# This is for the assertion part
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
