def sat(coords: List[List[int]], side=10, num_points=20):
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
    return {}

# We assume that the answer object is a dictionary with two keys: 'coords' and 'side'.
# 'coords' key stores the list of coordinates as tuples.
# 'side' key stores the side length of the grid.

def sol(side=10, num_points=20):
    coords = [(i, i) for i in range(side)]
    return {'coords': coords, 'side': side, 'num_points': num_points}

assert sat(sol().get('coords'))

if __name__ == "__main__":
    assert sat(sol())
