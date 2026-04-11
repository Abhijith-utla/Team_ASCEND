def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

def sol():
    return []

assert sat([])
assert not sat([[1, 0]])
assert not sat([[0, 1]])
assert not sat([[0, 0]])
assert not sat([[1, 1]])
assert not sat([[2, 0]])
assert not sat([[2, 1]])
assert not sat([[3, 0]])
assert not sat([[3, 1]])
assert not sat([[4, 0]])
assert not sat([[4, 1]])
assert not sat([[5, 0]])
assert not sat([[5, 1]])
assert not sat([[6, 0]])
assert not sat([[6, 1]])
assert not sat([[7, 0]])
assert not sat([[7, 1]])
assert not sat([[8, 0]])
assert not sat([[8, 1]])
assert not sat([[9, 0]])
assert not sat([[9, 1]])
assert

if __name__ == "__main__":
    assert sat(sol())
