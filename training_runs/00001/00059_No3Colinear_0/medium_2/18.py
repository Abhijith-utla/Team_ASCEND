def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for i, (x1, y1) in enumerate(coords):
        assert 0 <= x1 < side and 0 <= y1 < side
        for (x2, y2) in coords[i+1:]:
            assert x1 * (y2 - y1) != 0
    return len(coords) >= num_points

def sol():
    return []

# This is an example usage of the solution.
# You should replace it with your actual code.
assert sat([(0, 0), (5, 5), (10, 0), (0, 10)])
assert not sat([(0, 0), (5, 5), (10, 0)])
!python

if __name__ == "__main__":
    assert sat(sol())
