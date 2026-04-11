def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        assert x1 * (y2 - y1) != 0
    return len(coords) >= num_points

def sol():
    return []

# This is a simple example of how you can use the function.
# Note that you need to replace this with actual coordinates.
coords = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
assert sat(coords)

# It's important to note that the function will not work correctly if the side parameter is not set.
# If you want to ensure that the side parameter is set, you can simply replace the line with the following:
# side = 10
# assert sat(coords, side)

if __name__ == "__main__":
    assert sat(sol())
