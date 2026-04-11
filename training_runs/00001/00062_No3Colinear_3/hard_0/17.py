def sat(coords: List[List[int]], side=2, num_points=4):
    for i1 in range(len(coords)):
        x1, y1 = coords[i1]
        assert 0 <= x1 < side and 0 <= y1 < side
        for i2 in range(i1):
            x2, y2 = coords[i2]
            for i3 in range(i2):
                x3, y3 = coords[i3]
                assert x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# Checker:
def check(coords: List[List[int]], side=2, num_points=4):
    return sat(coords, side, num_points)

# Solver:
def solver(coords: List[List[int]], side=2, num_points=4):
    return []

# Test:
def test():
    assert check([[0, 0], [1, 1], [2, 2]]) == True
    assert check([[0, 0], [1, 2], [2, 2]]) == False
    assert check([[0, 0], [0, 1], [1, 1]]) == False
    assert check([[0, 0], [1, 0], [1, 1]]) == True
    assert check([[0, 0], [0, 1], [1, 1]], 3, 3) == True
    assert check([[0, 0], [0, 1], [1, 1]],

if __name__ == "__main__":
    assert sat(sol())
