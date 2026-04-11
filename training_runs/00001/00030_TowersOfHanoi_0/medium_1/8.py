def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return [8, 7, 6, 5, 4, 3, 2, 1]

print(sat([[0, 1], [1, 2], [2, 0], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]))
print(sat([[0, 3], [1, 2], [2, 0], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]))
print(sat([[0, 2], [1, 2], [2, 0], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]))
print(sat([[0, 1], [1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6]]))
print(sat([[0,

if __name__ == "__main__":
    assert sat(sol())
