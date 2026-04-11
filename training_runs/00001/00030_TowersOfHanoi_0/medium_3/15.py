def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[i].append(rods[j].pop())
        assert rods[i][-1] == min(rods[i]), "larger disk on top of smaller disk"
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8]

print(sat([[0, 7], [1, 6], [2, 5], [3, 4]]))  # [1, 2, 3, 4, 5, 6, 7, 8]
print(sat([[0, 1], [1, 2], [2, 3], [3, 0]]))  # [1, 2, 3, 4, 5, 6, 7, 8]
print(sat([[0, 3], [1, 2], [2, 1], [3, 2]]))  # [1, 2, 3, 4, 5, 6, 7, 8]
print(sat([[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]]))  # [1, 2, 3, 4, 5, 6,

if __name__ == "__main__":
    assert sat(sol())
