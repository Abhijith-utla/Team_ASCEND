def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return []

# Test cases
def test_case():
    assert sat([[0, 6], [1, 5], [0, 4], [3, 2], [2, 1], [3, 1]])
    assert not sat([[0, 6], [1, 5], [0, 4], [3, 2], [2, 1]])
    assert not sat([[0, 6], [1, 5], [0, 4]])
    assert sat([[2, 0], [1, 0], [3, 1], [2, 2], [2, 1], [3, 0]])

# Run tests
test_case()

if __name__ == "__main__":
    assert sat(sol())
