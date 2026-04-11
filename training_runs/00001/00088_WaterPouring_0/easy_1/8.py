def sat(moves, capacities=[8, 5, 3], init=[8, 0, 0], goal=[4, 4, 0]):
    state = init
    return state == goal

def sol():
    return [8, 0, 0]

if __name__ == "__main__":
    assert sat(sol())
