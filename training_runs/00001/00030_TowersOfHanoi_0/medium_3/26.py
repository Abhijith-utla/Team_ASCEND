def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[i].append(rods[j].pop())
        assert rods[i][-1] == min(rods[i]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8]

# Testing the solution
def test_sol():
    assert sat([])
    assert sat([[0, 7]])
    assert sat([[0, 6], [1, 5]])
    assert sat([[0, 5], [1, 4], [2, 3]])
    assert sat([[0, 4], [1, 3], [2, 2], [3, 1]])
    assert sat([[0, 3], [1, 2], [2, 1], [3, 0]])
    assert sat([[0, 2], [1, 1], [2, 0], [3, 3]])
    assert sat([[0, 1], [1, 0], [2, 3]])
    assert sat([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5,

if __name__ == "__main__":
    assert sat(sol())
