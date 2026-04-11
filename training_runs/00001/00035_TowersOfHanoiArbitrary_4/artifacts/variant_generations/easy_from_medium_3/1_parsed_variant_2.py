def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]
    for i, j in moves:
        state[i].append(state[j].pop())
        if sorted(state[i]) != target[i]:
            return False
    return sorted(state[0]) == target[0]

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
