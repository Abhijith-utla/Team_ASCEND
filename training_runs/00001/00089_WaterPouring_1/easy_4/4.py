def sat(moves, capacities=[724, 43, 611], init=[72, 2, 269], goal=[56, 0, 287]):
    state = init.copy()
    for move in moves:
        if state[move[0]] < capacities[move[1]]:
            state[move[0]], state[move[1]] = state[move[0]] + state[move[1]], capacities[move[1]]
        else:
            state[move[0]], state[move[1]] = capacities[move[1]], state[move[0]] + state[move[1]] - capacities[move[1]]
    return state == goal

def sol():
    return [724, 43, 611], [72, 2, 269], [56, 0, 287]

if __name__ == "__main__":
    assert sat(sol())
