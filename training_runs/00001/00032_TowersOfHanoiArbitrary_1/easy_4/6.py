def sat(moves: List[List[int]], source: List[List[int]], target: List[List[int]]):
    state = [s[:] for s in source]
    for move in moves:
        i, j = move[0], move[1]
        state[i].append(state[j].pop(0))
        assert sorted(state[j]) == target[i], 'State not sorted as expected'
    return state == target

def sol():
    return [[5, 4, 3], [2, 1, 6, 7], [8], []]

print(sat([[0, 1], [1, 0]], [[5, 4, 3], [2, 1, 6, 7], [8], []], [[5, 4, 3], [2, 1, 6, 7], [8], []]))  # Expected output: True
print(sat([[0, 1], [1, 0]], [[5, 4, 3], [2, 1, 6, 7], [8], []], [[5, 4, 3], [2, 6, 7], [8], []]))  # Expected output: False

if __name__ == "__main__":
    assert sat(sol())
