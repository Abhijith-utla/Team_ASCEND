def sat(moves: List[List[int]], source: List[List[int]], target: List[List[int]]):
    state = [s[:] for s in source]
    for move in moves:
        i, j = move[0], move[1]
        state[i].append(state[j].pop(0))
        assert sorted(state[j]) == sorted(target[i]), 'Sorted and sorted target not equal'
    return state == target

def sol():
    return []

# Tests
assert sat(
    moves=[[0, 0]],
    source=[[0, 2, 3]],
    target=[[2, 3, 0]]
)
assert not sat(
    moves=[[1, 0]],
    source=[[0, 2, 3]],
    target=[[2, 3, 1]]
)
assert sat(
    moves=[[0, 0], [0, 1]],
    source=[[0, 2, 3], [1, 2, 3]],
    target=[[2, 3, 0], [1, 2, 3]]
)
assert not sat(
    moves=[[1, 0], [0, 1]],
    source=[[0, 2, 3], [1, 2, 3]],
    target=[[2, 3, 1], [1, 2, 3]]
)
assert sat(
    moves=[[0, 0], [0,

if __name__ == "__main__":
    assert sat(sol())
