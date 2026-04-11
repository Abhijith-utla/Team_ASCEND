def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[i].append(rods[j].pop())
        if rods[i][-1] == min(rods[i]):
            rods[i].pop()
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return []

print(sat([[0, 1], [1, 0], [2, 1], [1, 2], [3, 0], [0, 3], [3, 2], [2, 3]]))  # should return True
print(sat([[0, 1], [1, 0], [2, 1], [1, 2], [3, 0], [0, 3], [3, 2], [2, 3], [4, 0], [0, 4], [4, 1], [1, 4], [4, 2], [2, 4], [4, 3], [3, 4]]))  # should return False

if __name__ == "__main__":
    assert sat(sol())
