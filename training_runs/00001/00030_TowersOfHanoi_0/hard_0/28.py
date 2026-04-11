def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

def sol():
    moves = [
        [3, 5],
        [4, 5],
        [2, 4],
        [1, 4],
        [0, 4],
        [0, 3],
        [1, 3],
        [2, 3],
        [4, 6],
        [5, 6],
        [3, 5]
    ]
    if sat(moves):
        return [8, 7, 6, 5, 4, 3, 2, 1, 0, 1]
    else:
        return []

print(sol())

if __name__ == "__main__":
    assert sat(sol())
