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
    return [[(0, 0), (1, 1), (2, 2), (3, 3)], [(0, 0), (1, 2), (2, 4), (3, 6)], [(0, 0), (1, 3), (2, 6), (3, 9)], [(0, 0), (1, 4), (2, 8), (3, 12)], [(0, 0), (1, 5), (2, 10), (3, 15)], [(0, 0), (1, 6), (2, 12), (3, 18)], [(0, 0), (1, 7), (2, 14), (3, 21)], [(0, 0), (1, 8), (2, 16), (3, 24)], [(0, 0), (1, 9), (2, 18), (3, 27)]]

print(sat

if __name__ == "__main__":
    assert sat(sol())
