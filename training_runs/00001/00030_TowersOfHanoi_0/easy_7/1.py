def sat(moves: List[List[int]]):
    rods = ([], [], [8, 7, 6, 5, 4, 3, 2, 1])
    for [i, j] in moves:
        rods[i].append(rods[j].pop())
        if rods[i][-1] == min(rods[i]):
            rods[i].append(rods[j].pop())
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

def sol():
    return [8, 7, 6, 5, 4, 3, 2, 1]

print(sat([]))
print(sat([[0, 7]]))
print(sat([[0, 1]]))
print(sat([[0, 6]]))
print(sat([[0, 2]]))
print(sat([[1, 3]]))
print(sat([[1, 4]]))
print(sat([[1, 5]]))
print(sat([[2, 0]]))
print(sat([[2, 1]]))
print(sat([[2, 6]]))
print(sat([[3, 0]]))
print(sat([[3, 1]]))
print(sat([[3, 5]]))
print(sat([[4, 0]]))
print(sat([[4, 2]]))
print(sat([[4, 5]]))
print(sat([[5, 0]]))
print(sat([[5, 1]]))
print

if __name__ == "__main__":
    assert sat(sol())
