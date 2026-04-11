def sat(moves: List[List[int]], source=[[0, 1, 2], [3], [4, 5, 6]], target=[[1, 2, 3], [4, 5], [0, 6]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[i].append(state[j].pop())
        assert state[i] == sorted(state[i])

    return state == target

def sol():
    class Answer:
        def __init__(self, state):
            self.state = state

    return Answer([s[:] for s in source])

print(sat([]))  # return True
print(sat([[0, 1, 2], [3], [4, 5, 6]]))  # return True
print(sat([[0, 1, 2], [3], [4, 5, 6]], [[1, 2, 3], [4, 5], [0, 6]]))  # return True
print(sat([[0, 1, 2], [3], [4, 5, 6]], [[1, 2, 3], [4, 5], [6, 0]]))  # return False
print(sat([[0, 1, 2], [3], [4, 5, 6]], [[1, 2, 3], [4, 5], [0, 6]]))  # return False

if __name__ == "__main__":
    assert sat(sol())
