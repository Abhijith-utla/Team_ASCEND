def sat(moves: List[List[int]], source=[[0, 1, 2, 3], [4], [5, 6, 7, 8, 9]], target=[[1, 2, 3, 8, 9], [4], [5]]):
    state = [s[:] for s in source]

    for move in moves:
        i, j = move[0], move[1]
        state[i].insert(0, state[j].pop(0))
        assert sorted(state[i]) == state[i]

    return state == target

def sol():
    moves = [
        [0, 1],
        [3, 1],
        [0, 2],
        [1, 0],
        [2, 3],
        [0, 0]
    ]
    source = [[0, 1, 2, 3], [4], [5, 6, 7, 8, 9]]
    target = [[1, 2, 3, 8, 9], [4], [5]]

    if sat(moves, source, target):
        return "valid"
    else:
        return "invalid"

# Uncomment this block to run the code and verify the solution
# print(sat(moves, source, target))

if __name__ == "__main__":
    assert sat(sol())
