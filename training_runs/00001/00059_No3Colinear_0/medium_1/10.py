def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for i1, (x1, y1) in enumerate(coords):
        assert 0 <= x1 < side and 0 <= y1 < side
        for i2, (x2, y2) in enumerate(coords):
            if i1 != i2:
                for i3, (x3, y3) in enumerate(coords):
                    if i2 != i3 and i1 != i3:
                        assert (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) != 0
    return len(coords) == num_points

def sol():
    return [], 0

if __name__ == "__main__":
    assert sat(sol())
