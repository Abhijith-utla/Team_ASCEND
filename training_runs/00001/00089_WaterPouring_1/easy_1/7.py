def sat(moves, capacities=[724, 43, 611], init=[72, 2, 269], goal=[56, 0, 287]):
    state = init.copy()

    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
