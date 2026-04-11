def sat(coords: List[List[int]], side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x >= 0 and x < side
        assert y >= 0 and y < side
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# Test case 1
assert sat([[0, 0]])

# Test case 2
assert not sat([[0, 0], [0, 1]])

# Test case 3
assert not sat([[0, 0], [1, 0]])

# Test case 4
assert sat([[0, 0], [1, 1]])

# Test case 5
assert sat([[0, 0], [0, 0]], side=2, num_points=2)

# Test case 6
assert not sat([[0, 0], [0, 0]], side=2, num_points=3)

if __name__ == "__main__":
    assert sat(sol())
