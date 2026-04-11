def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[j].append(state[i].pop(0))
        assert sorted(state[j]) == target[j], f'{state[j]} is not equal to {target[j]}'

    return state == target

def sol():
    return []

def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[j].append(state[i].pop(0))
        assert sorted(state[j]) == target[j], f'{state[j]} is not equal to {target[j]}'

    return state == target

if __name__ == "__main__":
    assert sat(sol())
