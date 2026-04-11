def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[6, 7], [0, 1, 2, 3], [4, 5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[j].append(state[i].pop(0))
        assert sorted(state[j]) == target[j]
    return state == target

def sol():
    return [source[:] for source in source]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
