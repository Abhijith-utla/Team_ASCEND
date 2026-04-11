def sat(coords: List[Tuple[int, int]], side=2, num_points=4):
    for i1, (x1, y1) in enumerate(coords):
        assert 0 <= x1 < side and 0 <= y1 < side
        for i2, (x2, y2) in enumerate(coords):
            if i1 == i2:
                continue
            for i3, (x3, y3) in enumerate(coords):
                if i2 == i3:
                    continue
                if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
                    return False
    return len(set(coords)) == num_points

def sol():
    return (0, 0), (1, 1), (2, 2), (3, 3)

if __name__ == "__main__":
    assert sat(sol())
