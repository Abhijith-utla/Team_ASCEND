def sat(moves: List[List[int]], source=[[0, 1, 2, 3], [4], [5, 6, 7, 8, 9]], target=[[1, 2, 3, 8, 9], [4], [5]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move[0], move[1]
        state[i].insert(0, state[j].pop(0))
        assert sorted(state[i]) == state[i]

    return state == target

def sol():
    return []

assert sat([])
assert not sat([[2,1,0,3,4]])
assert not sat([[0,1,2,3,4]])
assert sat([[1,2,3,0,4]])
assert not sat([[1,2,0,3,4]])
assert sat([[1,2,3,4,0]])
assert not sat([[3,2,1,4,0]])
assert sat([[3,2,4,1,0]])
assert not sat([[3,2,4,0,1]])
assert sat([[3,2,4,1,0]])
assert not sat([[2,1,3,0,4]])
assert sat([[2,1,3,4,0]])
assert not sat([[2,1,0,3,4]])
assert sat([[2,1,3,4,0]])
assert not sat([[1,2,0,3,4]])
assert sat([[1,2,3

if __name__ == "__main__":
    assert sat(sol())
