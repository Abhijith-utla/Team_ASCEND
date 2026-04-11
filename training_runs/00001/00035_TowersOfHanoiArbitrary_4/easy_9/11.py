def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [[s[0]] + s[1:] for s in source]
    for i, j in moves:
        state[i].append(state[j].pop())
        if sorted(state[i]) != target[i]:
            return False
    return all(sorted(s) == target[i] for i, s in enumerate(state))

def sol():
    return [5, 6, 1, 2, 4, 0, 3, 2, 3, 4, 6, 0, 1, 5]

# For the checker to pass
assert sat(source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]])

if __name__ == "__main__":
    assert sat(sol())
