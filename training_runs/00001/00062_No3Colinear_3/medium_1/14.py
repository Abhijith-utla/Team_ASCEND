def sat(coords: List[List[int]], side=2, num_points=4):
    for i1 in range(len(coords)):
        x1, y1 = coords[i1]
        assert 0 <= x1 < side and 0 <= y1 < side
        for i2 in range(i1):
            x2, y2 = coords[i2]
            for i3 in range(i2):
                x3, y3 = coords[i3]
                if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
                    return False
    return len({(a, b) for a, b in coords}) == num_points

def sol():
    return []

# Test case 1: All points on same line
coords = [(0,0), (1,1), (2,2), (3,3)]
assert sat(coords)

# Test case 2: Two points on same line and one not
coords = [(0,0), (1,1), (2,2), (3,3), (4,4)]
assert not sat(coords)

# Test case 3: Three points on same line, two of which are on same line and one not
coords = [(0,0), (1,1), (2,2), (3,3), (4,4), (5,5)]
assert not sat(coords)

# Test case 4: Four points on same line, three of which are on same line and two of which are not
coords = [(0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
assert not sat(coords)

# Test case 5:

if __name__ == "__main__":
    assert sat(sol())
