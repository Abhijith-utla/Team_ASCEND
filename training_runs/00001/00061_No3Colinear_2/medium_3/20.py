def sat(coords: List[List[int]], side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x == y
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# Testing
coords = [[2, 2], [3, 3]]
assert sat(coords)

coords = [[2, 3], [3, 4]]
assert not sat(coords)

coords = [[2, 3]]
assert not sat(coords)

coords = [[2, 3], [2, 3]]
assert sat(coords)

coords = [[2, 3]]
assert sat(coords, num_points=2)

coords = [[2, 3]]
assert sat(coords, side=2)

if __name__ == "__main__":
    assert sat(sol())
