def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[i].append(rods[j].pop())
        if rods[i][-1] == min(rods[i]):
            rods[i].pop()
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8]

# This function is used for testing the correctness of the solution
def test_sol():
    assert sat([])
    assert sat([[0, 7]])
    assert sat([[0, 1], [1, 2]])
    assert sat([[0, 1], [1, 0]])
    assert sat([[0, 2], [1, 0], [2, 1]])
    assert sat([[0, 2], [1, 0], [2, 2]])
    assert sat([[0, 2], [1, 1]])
    assert sat([[0, 2], [1, 1], [2, 2]])
    assert sat([[0, 3], [1, 0], [2, 1], [3, 2]])
    assert sat([[0, 3], [1, 1], [2, 2], [3, 3]])

if __name__ == "__main__":
    assert sat(sol())
