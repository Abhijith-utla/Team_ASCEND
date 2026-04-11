def sat(coords: List[List[int]], side=1, num_points=1):
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

# This function will never be called because the input coords array is empty
assert sat([])

# Test with a single point
assert not sat([(0, 0)])

# Test with two points on the same line
assert not sat([(0, 0), (1, 1)])

# Test with three points in different order
assert sat([(1, 1), (0, 0), (2, 2)])

# Test with a line with two points
assert sat([(0, 0), (2, 2)])

# Test with a line with three points
assert sat([(0, 0), (2, 2), (3, 3)])

# Test with a line with four points
assert not sat([(0, 0), (2, 2), (3, 3), (1, 1)])

# Test with a line with five points
assert not sat([(0, 0), (2, 2), (3, 3), (1, 1), (4, 4

if __name__ == "__main__":
    assert sat(sol())
