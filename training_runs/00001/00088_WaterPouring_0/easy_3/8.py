def sat(moves, capacities=[8, 5, 3], init=[8, 0, 0], goal=[4, 4, 0]):
    state = init
    for move in moves:
        n = min(capacities[move[1]], state[move[0]] + state[move[1]])
        state[move[0]], state[move[1]] = state[move[0]] + state[move[1]] - n, n
    return state == goal

def sol():
    return [8, 0, 0]

assert sat([])
assert not sat([(0, 1)])
assert not sat([(0, 1), (1, 2)])
assert sat([(0, 0)])
assert sat([(0, 1), (1, 2), (2, 0)])
assert not sat([(0, 1), (0, 2)])
assert not sat([(0, 1), (1, 0)])
assert not sat([(0, 1), (1, 1)])
assert sat([(0, 0), (1, 1), (2, 2)])
assert not sat([(0, 0), (1, 0), (2, 0)])
assert not sat([(0, 1), (1, 0), (0, 2)])
assert not sat([(0, 0), (0, 1), (1, 1)])
assert sat([(0, 0), (0, 1), (0, 2

if __name__ == "__main__":
    assert sat(sol())
