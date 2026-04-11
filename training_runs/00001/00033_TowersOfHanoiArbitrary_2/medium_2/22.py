def sat(moves: List[List[int]], source=[[0, 1, 2, 7, 8], [3], [4, 5, 6]], target=[[1, 2, 3, 8], [4, 5], [0, 6]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    class Answer:
        def __init__(self, state):
            self.state = state

    moves = [(i, j) for i in range(5) for j in range(len(i))]
    return Answer(source) if sat(moves) else Answer(target)

if __name__ == "__main__":
    assert sat(sol())
