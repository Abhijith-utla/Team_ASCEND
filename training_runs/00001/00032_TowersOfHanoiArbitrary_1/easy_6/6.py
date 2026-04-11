def sat(moves: List[List[int]], source: List[List[int]], target: List[List[int]]):
    state = [s[:] for s in source]
    for move in moves:
        i, j = move[0], move[1]
        state[i].append(state[j].pop(0))
        assert sorted(state[j]) == sorted(target[i]) and sorted(state[j]) == sorted(target[i]), 'Sorted and sorted target not equal'
    return state == target

def sol():
    return []

def sat(moves: List[List[int]], source: List[List[int]], target: List[List[int]]):
    state = [s[:] for s in source]
    for move in moves:
        i, j = move[0], move[1]
        state[i].append(state[j].pop(0))
        assert sorted(state[j]) == sorted(target[i]) and sorted(state[j]) == sorted(target[i]), 'Sorted and sorted target not equal'
    return state == target

# Test cases
print(sat([[0,1]], [[3],[2,1,0]], [[2,1,3],[0]])) # False
print(sat([[0,1]], [[1,2,3],[0]], [[2,1,3],[0]])) # True

if __name__ == "__main__":
    assert sat(sol())
