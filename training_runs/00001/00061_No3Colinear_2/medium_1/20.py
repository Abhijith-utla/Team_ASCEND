def sat(coords: List[List[int]], side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x >= 0 and x < side
        assert y >= 0 and y < side
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# Test case 1: All points on a single line
assert sat([[0, 0]])

# Test case 2: All points on a line
assert sat([[0, 0], [1, 0], [0, 1]])

# Test case 3: Some points on a line
assert not sat([[0, 0], [1, 0], [0, 1], [2, 2]])

# Test case 4: All points on a diagonal
assert sat([[0, 0], [1, 1], [2, 2]])

# Test case 5: Some points on a diagonal
assert not sat([[0, 0], [1, 1], [2, 2], [3, 3]])

# Test case 6: Empty set
assert sat([])

# Test case 7: Set with no points
assert not sat([[0, 0]])

# Test case 8: Set with one point
assert sat([[0, 0], [1,

if __name__ == "__main__":
    assert sat(sol())
