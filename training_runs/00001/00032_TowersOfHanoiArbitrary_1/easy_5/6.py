def sat(moves: List[List[int]], source: List[List[int]], target: List[List[int]]):
    state = [s[:] for s in source]
    for move in moves:
        i, j = move[0], move[1]
        state[i].append(state[j].pop(0))
        assert sorted(state[j]) == sorted(target[i]), 'Sorted and sorted target not equal'
    return state == target

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
