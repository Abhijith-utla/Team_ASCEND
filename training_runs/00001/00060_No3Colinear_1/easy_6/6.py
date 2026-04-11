def sat(coords: List[List[int]], side=0, num_points=0):
    for i1 in range(len(coords)):
        x1, y1 = coords[i1]
        assert 0 <= x1 < side
        for i2 in range(i1 + 1, len(coords)):
            x2, y2 = coords[i2]
            assert 0 <= y2 < side
            for i3 in range(i2 + 2, len(coords)):
                x3, y3 = coords[i3]
                assert x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0
    return len({(a, b) for a, b in coords}) >= num_points

def sol(coords: List[Tuple[int, int]], side=0, num_points=0):
    coords.append((0, 0))
    for i in range(len(coords)):
        x, y = coords[i]
        assert 0 <= x < side
        for j in range(i + 1, len(coords)):
            u, v = coords[j]
            assert 0 <= v < side
            for k in range(j + 2, len(coords)):
                w, z = coords[k]
                assert (x * (v - y) + u * (y - v) + w * (v - u)) != 0
    return len({(a, b) for a, b in coords}) >= num_points

def test():
    assert sat([(0, 0)]) == False
    assert sat([(0, 0), (1, 1)]) == False
    assert sat([(0, 0), (1, 1), (2, 2)]) == False
    assert

if __name__ == "__main__":
    assert sat(sol())
