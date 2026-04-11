def sat(moves: List[List[int]]):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop())
        assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
    return rods[0] == rods[1] == []

def sol():
    class Answer:
        def __init__(self, moves):
            self.moves = moves

    def sat(moves: List[List[int]]):
        rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
        for [i, j] in moves:
            rods[j].append(rods[i].pop())
            if rods[j][-1] > min(rods[j]):
                return False
        return rods[0] == rods[1] == []

    moves = [[0, 1], [1, 2], [2, 0], [0, 3], [3, 1], [1, 4], [4, 5], [5, 6], [6, 7]]
    answer = Answer(moves)
    return answer

print(sol().moves)

if __name__ == "__main__":
    assert sat(sol())
