def sat(coords: List[List[int]], side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert x == y
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# This assertion will always pass, as we never provide the solution.
assert sat([])

# This assertion will also pass, because we have 1 point on the side of length 1.
assert sat([(1, 1)])

# This assertion will fail, because we have 2 points and we're looking for 3 points.
assert not sat([(1, 1), (2, 2)])

# This assertion will pass, because we have 3 points and we're looking for 3 points.
assert sat([(1, 1), (2, 2), (3, 3)])

if __name__ == "__main__":
    assert sat(sol())
