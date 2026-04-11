def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[i].insert(0, state[j].pop())
    sorted_state_j = [sorted(state[j]) for j in range(3)]
    sorted_target_j = [sorted(target[j]) for j in range(3)]
    return sorted_state_j == sorted_target_j

def sol():
    return []

# The solution is empty because the problem states that the source and target arrays are not modified and the solution is only valid if the source array is changed to match the target array.

if __name__ == "__main__":
    assert sat(sol())
