def sat(coords: List[List[int]], side=0, num_points=0):
    for i1 in range(len(coords)):
        x1, y1 = coords[i1]
        assert 0 <= x1 < side
        for i2 in range(i1):
            x2, y2 = coords[i2]
            assert 0 <= y2 < side
            for i3 in range(i2):
                x3, y3 = coords[i3]
                assert x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0
    return len({(a, b) for a, b in coords}) == num_points and len(coords) == len(set(tuple(sorted(coord)) for coord in coords))

def sol(coords: List[List[int]], side=0, num_points=0):
    def check_point(x, y, coords):
        for (x1, y1) in coords:
            if (x1 - x) * (y - y1) == (x - x1) * (y1 - y):
                return False
        return True

    def check_segment(x1, y1, x2, y2, coords):
        for (x, y) in coords:
            if (x < x1 or x > x2 or y < y1 or y > y2):
                continue
            if check_point(x, y, [(x1, y1), (x2, y2)]) is False:
                return False
        return True

    def check_triangle(x1, y1, x2, y2, x3, y3, coords):
        if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) !

if __name__ == "__main__":
    assert sat(sol())
