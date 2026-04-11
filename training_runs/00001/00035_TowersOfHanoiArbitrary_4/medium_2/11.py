def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[i].append(state[j].pop(0))
        assert sorted(state[i]) == target[i], f'{state[i]} is not equal to {target[i]}'

    return state == target

def sol():
    return []

def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[i].append(state[j].pop(0))
        assert sorted(state[i]) == target[i], f'{state[i]} is not equal to {target[i]}'

    return state == target

# Checker runs:
assert sat([])
!pip install pytest
assert not sat([])

if __name__ == "__main__":
    assert sat(sol())
