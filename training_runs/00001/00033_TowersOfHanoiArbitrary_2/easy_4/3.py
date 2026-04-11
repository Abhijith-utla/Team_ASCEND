def sat(moves: List[List[int]], source=[[0, 1, 2, 7, 8], [3], [4, 5, 6]], target=[[1, 2, 3, 8], [4, 5], [0, 6]]):
    state = [s[:] for s in source]

    for move in moves:
        state[move[1]].append(state[move[0]].pop())
        assert sorted(state[move[1]]) == state[move[1]]

    return state == target

def sol():
    return [sorted(s) for s in [[] for _ in range(9)]]

print(sat([[0,1,2,7,8],[3],[4,5,6]], sol()))
print(sat([[1,2,3,8],[4,5],[0,6]]))
print(sat([[0,1,2,7,8],[3],[4,5,6]], [[1,2,3,8],[4,5],[0,6]], [[1,2,3,6,8],[4,5],[0]]))
print(sat([[1,2,3,8],[4,5],[0,6]], [[0,1,2,7,8],[3],[4,5,6]], [[1,2,3,8],[4,5],[0]]))
print(sat([[0,1,2,7,8],[3],[4,5,6]], [[1,2,3,8],[4,5],[0,

if __name__ == "__main__":
    assert sat(sol())
