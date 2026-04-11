def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[i].insert(0, state[j].pop())
    sorted_state_j = [sorted(state[j]) for j in range(3)]
    sorted_target_j = [sorted(target[j]) for j in range(3)]
    return sorted_state_j == sorted_target_j

def sol():
    return [[5, 6], [1, 2, 4], [0, 3]], [[2, 3, 4, 6], [0, 1], [5]]

# Test case
print(sat([[[5, 6], [1, 2, 4], [0, 3]], [[2, 3, 4, 6], [0, 1], [5]]])) # Should return True
print(sat([[[5, 6], [1, 2, 4], [0, 3]], [[2, 3, 4, 6], [1, 0], [5]]])) # Should return False

if __name__ == "__main__":
    assert sat(sol())
