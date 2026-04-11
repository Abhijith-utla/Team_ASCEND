def sat(moves: List[List[int]], source=[[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]], target=[[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [
        [[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]],
        [[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]],
    ]


def test_sat():
    assert sat(moves=[[0, 2], [1, 3]])
    assert not sat(moves=[[0, 2], [3, 1]])
    assert sat(moves=[[0, 2], [1, 3], [0, 1]])
    assert not sat(moves=[[0, 2], [3, 1], [0, 1], [1, 2]])
    assert sat(moves=[[0,

if __name__ == "__main__":
    assert sat(sol())
