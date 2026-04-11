def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    moves = [[5, 6], [1, 2, 4], [0, 3]]
    source = [[5, 6], [1, 2, 4], [0, 3]]
    target = [[2, 3, 4, 6], [0, 1], [5]]

    if sat(moves, source, target):
        return "Yes"
    else:
        return "No"

print(sol())

if __name__ == "__main__":
    assert sat(sol())
