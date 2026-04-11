def sat(coords: List[List[int]], side=0, num_points=0):
    for i1 in range(len(coords)):
        x1, y1 = coords[i1]
        assert 0 <= x1 < side
        for i2 in range(i1):
            x2, y2 = coords[i2]
            assert 0 <= y2 < side
            for i3 in range(i2):
                x3, y3 = coords[i3]
                assert (y1 - y2) * (x2 - x3) == (y3 - y1) * (x3 - x2)
    return len({(a, b) for a, b in coords}) == num_points

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
