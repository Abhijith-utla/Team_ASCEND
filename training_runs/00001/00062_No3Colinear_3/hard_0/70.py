def sat(coords: List[List[int]], side=2, num_points=4):
    for i1 in range(len(coords)):
        x1, y1 = coords[i1]
        assert 0 <= x1 < side and 0 <= y1 < side
        for i2 in range(i1):
            x2, y2 = coords[i2]
            for i3 in range(i2):
                x3, y3 = coords[i3]
                assert x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# The function is correct but it will fail the assert statement inside the loop.
# The correct solution is to create a list of coordinates and then pass it to the function.
# I'm assuming the function is working correctly if the problem is solved properly.
# If it fails, the solution must be different.

# Example:
# If we have a square with sides of 2, we need 4 points to make a polygon.
# If the function is not solving correctly, it should return False.
# And if it is, it should return True.

# Testing the function with the example:
assert not sat([[0, 0], [1, 0], [1, 1], [0, 1]])
assert sat([[0, 0], [1, 0], [1, 1], [0, 1], [1, 2], [2, 2]])

if __name__ == "__main__":
    assert sat(sol())
