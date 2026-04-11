def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]
    for move in moves:
        state[move[0]].append(state[move[1]].pop())
    return sorted(state[0]) == target[0]

def sol():
    return []

assert sat([])
assert not sat([[0, 1]])
assert not sat([[0, 1], [1, 0]])
assert sat([[0, 1], [2, 0]])
assert not sat([[0, 1], [0, 2]])
assert not sat([[0, 1], [1, 0], [2, 0]])
assert sat([[0, 1], [1, 0], [2, 0], [2, 3]])
assert not sat([[0, 1], [1, 0], [2, 0], [2, 3], [3, 2]])
assert sat([[0, 1], [1, 0], [2, 0], [2, 3], [3, 2], [3, 1]])
assert not sat([[0, 1], [1, 0], [2, 0], [2, 3], [3, 2], [3, 1], [1, 2]

if __name__ == "__main__":
    assert sat(sol())
