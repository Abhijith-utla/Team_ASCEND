def sat(moves: List[List[int]], source=[[0, 1, 2], [3], [4, 5, 6]], target=[[1, 2, 3], [4, 5], [0, 6]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[i].append(state[j].pop())
        assert state[i] == sorted(state[i])

    return state == target

def sol():
    class Answer:
        pass

    answer = Answer()
    answer.state = [[0, 1, 2], [3], [4, 5, 6]]

    return answer

# Checker
def check(moves: List[List[int]], source=[[0, 1, 2], [3], [4, 5, 6]], target=[[1, 2, 3], [4, 5], [0, 6]]):
    assert sol() == Answer()

# Run checks
check()

if __name__ == "__main__":
    assert sat(sol())
