def sat(moves: List[List[int]], source=[[0, 1, 2, 7, 8], [3], [4, 5, 6]], target=[[1, 2, 3, 8], [4, 5], [0, 6]]):
    state = [s[:] for s in source]
    for move in moves:
        state[move[1]].append(state[move[0]].pop())
        state[move[1]] = sorted(state[move[1]])

    return state == target

def sol(moves):
    def sat(state):
        state_copy = [s[:] for s in state]
        for move in moves:
            state_copy[move[1]].append(state_copy[move[0]].pop())
            state_copy[move[1]] = sorted(state_copy[move[1]])
        return state_copy == target

    return sat

if __name__ == "__main__":
    assert sat(sol())
