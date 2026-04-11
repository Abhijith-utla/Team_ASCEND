def sat(moves: List[List[int]], source=[[0, 1, 2, 3], [4], [5, 6, 7, 8, 9]], target=[[1, 2, 3, 8, 9], [4], [5]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move[0], move[1]
        state[i].insert(0, state[j].pop(0))
        assert sorted(state[i]) == state[i]

    return state == target

def sol():
    return [
        [0, 1, 2, 3],
        [4],
        [5, 6, 7, 8, 9]
    ]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
