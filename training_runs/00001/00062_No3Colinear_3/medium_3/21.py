def sat(coords: List[List[int]], side=2, num_points=4):
    for i1 in range(len(coords)):
        x1, y1 = coords[i1]
        assert 0 <= x1 < side and 0 <= y1 < side
        for i2 in range(i1):
            x2, y2 = coords[i2]
            for i3 in range(i2):
                x3, y3 = coords[i3]
                if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) != 0:
                    return False
    return len({(a, b) for a, b in coords}) == num_points

def sol():
    return []

# The provided function is incorrect.
# The function expects a list of coordinates, but the example provided does not contain coordinates.
# Therefore, we can create a valid solution for the problem by providing some coordinates.
# We create a list of 4 points on a 2x2 grid.
def sol():
    return [(0,0), (0,1), (1,0), (1,1)]

# The provided function is incorrect.
# The function is supposed to check if the given points are on the same line, 
# but the example provided does not include any points.
# Therefore, we can create a valid solution for the problem by providing some points.
# We create a list of 4 points on a 2x2 grid.
def sol():
    return [(0,0), (0,1), (1,0), (1,1)]

if __name__ == "__main__":
    assert sat(sol())
