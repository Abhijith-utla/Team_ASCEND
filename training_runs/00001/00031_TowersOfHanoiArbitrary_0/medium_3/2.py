def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 7], [1, 2, 3], [4, 5, 6]]):
    state = [s[:] for s in source]

    for i, j in moves:
        state[j].append(state[i].pop())
        assert sorted(state[j]) == target[j]

    return state == target

def sol():
    return []

# Testing
def test_sat():
    assert sat([[0,7],[4,5,6],[1,2,3,8]],[[0,7],[1,2,3],[4,5,6]])
    assert not sat([[0,7],[4,5,6],[1,2,3,8]],[[0,7],[1,2,3],[4,6,5]])
    assert sat([[0,7,8],[1,2,3,4,5,6],[7]],[[0,7,8],[1,2,3,4,5,6],[7]])
    assert not sat([[0,7,8],[1,2,3,4,5,6],[7]],[[0,7,8],[1,2,3,4,5,6],[6,7]])

test_sat()

if __name__ == "__main__":
    assert sat(sol())
