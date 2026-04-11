def sat(moves: List[List[int]], capacities=[357, 298, 492], init=[8, 284, 70], goal=[0, 0, 364]):
    state = init.copy()

    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"

def sol():
    return [357, 298, 492]

if __name__ == "__main__":
    assert sat(sol())
