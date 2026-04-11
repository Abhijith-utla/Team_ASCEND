def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[i].append(state[j].pop(0))
        assert sorted(state[i]) == target[i], f'{state[i]} is not equal to {target[i]}'

    return state == target

def sol():
    return [
        [5, 6, 0],
        [1, 2, 4, 3],
        [0]
    ]

assert sat(moves=[[0, 0], [1, 1], [2, 2]])
assert not sat(moves=[[0, 1], [1, 2], [2, 0]])
assert sat(moves=[[0, 2], [1, 0], [2, 1]])
assert not sat(moves=[[0, 2], [1, 0], [3, 2]])

if __name__ == "__main__":
    assert sat(sol())
