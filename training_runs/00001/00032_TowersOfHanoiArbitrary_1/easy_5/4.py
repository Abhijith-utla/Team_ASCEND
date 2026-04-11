def sat(moves: List[List[int]], source: List[List[int]], target: List[List[int]]):
    state = [s[:] for s in source]
    for move in moves:
        i, j = move[0], move[1]
        state[i].append(state[j].pop(0))
        assert sorted(state[j]) == sorted(target[i]), 'Sorted and sorted target not equal'
    return state == target

def sol():
    return []

print(sat([], [], []))
print(sat([[0, 1, 2], [1, 2, 0]], [[1, 2, 0], [2, 0]], [[2, 0], [1, 2, 0]]))
print(sat([[0, 1, 2], [1, 2, 0]], [[2, 0], [1, 2, 0]], [[2, 0], [1, 2, 0]]))
print(sat([[0, 1, 2], [1, 2, 0]], [[0, 2, 1], [2, 0]], [[2, 0], [0, 1, 2]]))
print(sat([[0, 1, 2], [1, 2, 0]], [[2, 0], [0, 1, 2]], [[2, 0], [1, 2, 0]]))

if __name__ == "__main__":
    assert sat(sol())
