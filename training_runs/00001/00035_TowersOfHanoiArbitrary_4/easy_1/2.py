def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[j].append(state[i].pop(0))
    sorted_state_j = [sorted(state[j]) for j in range(3)]
    sorted_target_j = [sorted(target[j]) for j in range(3)]
    return sorted_state_j == sorted_target_j

def sol():
    return [5, 6], [[1, 2, 4], [0, 3], [5]]

print(sat([[5, 6], [1, 2, 4], [0, 3]]))
print(sat([[2, 3, 4, 6], [0, 1], [5]]))
print(sat([[2, 3, 4, 6], [1, 0], [5, 7, 8]]))
print(sat([[1, 2, 3, 4, 5], [0, 6], [7]]))
print(sat([[0, 1, 2, 3, 4], [5, 6, 7, 8], [9]]))
print(sat([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10]]))
print(sat([[0, 1, 2, 3, 4], [5, 6, 7, 8,

if __name__ == "__main__":
    assert sat(sol())
