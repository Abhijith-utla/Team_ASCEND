def sat(coords: List[List[int]], side=2, num_points=4):
    for i1 in range(len(coords)):
        x1, y1 = coords[i1]
        assert 0 <= x1 < side and 0 <= y1 < side
        for i2 in range(i1):
            x2, y2 = coords[i2]
            for i3 in range(i2):
                x3, y3 = coords[i3]
                if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
                    return True
    return len({(a, b) for a, b in coords}) >= num_points

def sol():
    return [1, 2, 3, 4, 5, 6]

# Test code
assert sat([(1, 1), (2, 2), (3, 3), (4, 4)])
assert not sat([(0, 0), (1, 1), (2, 2), (3, 3)])
assert sat([(0, 0), (1, 1), (0, 2), (1, 3)])
assert not sat([(0, 0), (1, 1), (0, 2), (2, 2)])

if __name__ == "__main__":
    assert sat(sol())
