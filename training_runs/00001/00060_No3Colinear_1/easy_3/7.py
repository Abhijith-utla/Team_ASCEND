def sat(coords: List[List[int]], side=0, num_points=0):
    for i1 in range(len(coords)):
        x1, y1 = coords[i1]
        assert 0 <= x1 < side
        for i2 in range(i1):
            x2, y2 = coords[i2]
            assert 0 <= y2 < side
            for i3 in range(i2):
                x3, y3 = coords[i3]
                assert x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) == x1 * y2 + x2 * y3 + x3 * y1
    return len({(a, b) for a, b in coords}) == num_points

def sol(side=0, num_points=0):
    coords = [(0, 0)]
    while len(coords) < side:
        x, y = coords[-1]
        nx, ny = x + 1, y + 1
        if nx < side:
            coords.append((nx, ny))
        else:
            if ny < side:
                coords.append((nx, ny))
            else:
                if nx == num_points and ny == num_points:
                    return len(coords)
                else:
                    coords = [(0, 0)]
                    continue
    return len({(a, b) for a, b in coords}) == num_points

# Test
assert sol(4, 4)
assert sol(5, 5)
assert sol(6, 6)
assert sol(7, 7)
assert sol(8, 8)
assert sol(10, 10)
assert sol(100, 100)

if __name__ == "__main__":
    assert sat(sol())
