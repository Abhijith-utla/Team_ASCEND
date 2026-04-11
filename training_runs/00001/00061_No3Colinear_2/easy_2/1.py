def sat(coords: List[List[int]], side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x >= 0 and x < side
        assert y >= 0 and y < side
    return len({(a+1, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# Test
coords = [[0, 0], [0, 1], [1, 1], [1, 0]]
assert sat(coords)

coords = [[0, 0]]
assert not sat(coords)

coords = [[0, 0], [0, 1], [1, 1], [1, 2]]
assert not sat(coords)

coords = [[0, 0], [0, 1], [1, 1]]
assert sat(coords)

if __name__ == "__main__":
    assert sat(sol())
