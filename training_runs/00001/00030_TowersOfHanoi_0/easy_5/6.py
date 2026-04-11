def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[j].insert(0, rods[i].pop())
        if rods[j][-1] == min(rods[j]):
            return False
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return [8, 7, 6, 5, 4, 3, 2, 1]

# print(sat([[0, 5], [1, 4], [2, 3], [3, 2], [4, 1], [5, 0]])) # [8, 7, 6, 5, 4, 3, 2, 1]
# print(sat([[0, 6], [1, 5], [2, 4], [3, 3], [4, 2], [5, 1], [6, 0]])) # [8, 7, 6, 5, 4, 3, 2, 1]
# print(sat([[1, 2], [2, 1], [3, 0], [4, 3], [5, 4], [6, 5], [7, 6]])) # [8, 7, 6, 5, 4, 3, 2, 1]
# print(sat([[3,

if __name__ == "__main__":
    assert sat(sol())
