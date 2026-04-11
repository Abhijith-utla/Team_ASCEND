def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [[s[0]] + s[1:] for s in source]
    for i, j in moves:
        state[i].append(state[j].pop())
        if sorted(state[i]) != target[i]:
            return False
    return all(sorted(s) == target[i] for i, s in enumerate(state))

def sol():
    return []

# Test case 1
moves = [[0, 2], [1, 0], [2, 1]]
source = [[5, 6], [1, 2, 4], [0, 3]]
target = [[6, 5, 4], [1, 2, 3], [0]]
assert sat(moves, source, target)

# Test case 2
moves = [[0, 2], [1, 0], [1, 2], [2, 0]]
source = [[1, 2], [3], [0, 4, 5]]
target = [[2, 1, 3, 0], [4, 5], [0]]
assert sat(moves, source, target)

# Test case 3
moves = [[1, 0], [0, 1]]
source = [[2, 3, 5, 4], [1, 6, 7, 8], [0, 3]]
target = [[3, 5, 4, 2

if __name__ == "__main__":
    assert sat(sol())
