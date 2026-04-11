def sat(moves: List[List[int]], capacities=[8, 5, 3], init=[8, 0, 0], goal=[4, 4, 0]):
    state = init.copy()

    for [i, j] in moves:
        assert min(i, j) >= 0, "Indices must be non-negative"
        assert i != j, "Cannot pour from same state to itself"
        n = min(capacities[j], state[i] + state[j])
        state[i], state[j] = state[i] + state[j] - n, n

    return state == goal

def sol():
    return [8, 0, 0]

print(sat([[1,2],[3,4],[4,0],[1,3],[2,1]]))
print(sat([[1,2],[3,4],[4,0],[1,3],[2,0]]))
print(sat([[2,0],[3,4],[4,0],[1,3],[2,1]]))
print(sat([[1,0],[3,4],[4,0],[1,3],[2,1]]))
print(sat([[2,1],[3,4],[4,0],[1,3],[0,1]]))
print(sat([[1,2],[3,5],[4,0],[1,3],[2,1]]))
print(sat([[1,2],[3,4],[5,0],[1,3],[2,1]]))

if __name__ == "__main__":
    assert sat(sol())
