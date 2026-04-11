def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[3, 2, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[i].append(state[j].pop(0))
        assert sorted(state[i]) == sorted(target[i]), f'{sorted(state[i])} is not equal to {sorted(target[i])}'

    return sorted(state) == sorted(target)

def sol():
    moves = [[0, 1], [1, 2], [2, 3]]
    source = [[5, 6], [1, 2, 4], [0, 3]]
    target = [[3, 2, 4, 6], [0, 1], [5]]
    return moves

if __name__ == "__main__":
    assert sat(sol())
