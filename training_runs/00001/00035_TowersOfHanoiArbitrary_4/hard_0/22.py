def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [source[:], target[:]]

# Test case
def test():
    moves = [(0, 1), (1, 2), (2, 0), (1, 0)]
    source = [[5, 6], [1, 2, 4], [0, 3]]
    target = [[2, 3, 4, 6], [0, 1], [5]]
    assert sat(moves, source, target)

test()

if __name__ == "__main__":
    assert sat(sol())
