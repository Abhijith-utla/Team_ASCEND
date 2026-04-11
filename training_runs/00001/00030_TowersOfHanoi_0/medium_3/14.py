def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[i].append(rods[j].pop())
        assert rods[i][-1] == min(rods[i]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return [[], [], [8, 7, 6, 5, 4, 3, 2, 1]]

print(sat([]))
print(sat([[0, 0]]))
print(sat([[0, 1]]))
print(sat([[1, 0]]))
print(sat([[1, 1]]))
print(sat([[2, 2]]))
print(sat([[2, 3]]))
print(sat([[3, 2]]))
print(sat([[3, 3]]))
print(sat([[4, 4]]))
print(sat([[4, 5]]))
print(sat([[5, 4]]))
print(sat([[5, 5]]))
print(sat([[6, 6]]))
print(sat([[6, 7]]))
print(sat([[7, 6]]))
print(sat([[7, 7]]))
print(sat([[0, 0], [1, 1], [2, 2],

if __name__ == "__main__":
    assert sat(sol())
