def sat(coords, side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert 0 <= x < side
        assert 0 <= y < side
    return len({(a, b) for a, b in coords}) == len(coords) - num_points

def sol():
    return []

# Test case 1
coords1 = [(0, 0), (0, 1), (0, 2)]
assert sat(coords1, 2, 1)

# Test case 2
coords2 = [(0, 0), (1, 1), (2, 2)]
assert not sat(coords2, 3, 1)

# Test case 3
coords3 = [(0, 0), (1, 0), (1, 1)]
assert sat(coords3, 2, 1)

# Test case 4
coords4 = [(0, 0), (1, 1), (0, 2)]
assert not sat(coords4, 3, 1)

# Test case 5
coords5 = [(0, 0), (1, 1), (1, 2)]
assert not sat(coords5, 2, 1)

# Test case 6
coords6 = [(0, 0), (0

if __name__ == "__main__":
    assert sat(sol())
