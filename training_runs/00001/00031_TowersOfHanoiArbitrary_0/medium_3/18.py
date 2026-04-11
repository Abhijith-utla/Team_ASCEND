def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 7], [1, 2, 3], [4, 5, 6]]):
    state = [s[:] for s in source]

    for i, j in moves:
        state[j].append(state[i].pop())
        assert sorted(state[j]) == target[j]

    return state == target

def sol():
    return [
        [[4, 5, 6], [0, 7], [1, 2, 3, 8]],
        [[0, 7], [1, 2, 3], [4, 5, 6]],
        [[0, 7], [4, 5, 6], [1, 2, 3, 8]],
        [[0, 7], [1, 2, 3], [4, 5, 6]]
    ]


print(sat(moves=[[0, 2], [3, 1]]))  # False
print(sat(moves=[[1, 2], [3, 0]]))  # False
print(sat(moves=[[1, 2], [3, 4], [0, 7]]))  # False
print(sat(moves=[[0, 2], [3, 1], [4, 5, 6]]))  # True
print(sat(moves=[[2, 1], [0, 3],

if __name__ == "__main__":
    assert sat(sol())
