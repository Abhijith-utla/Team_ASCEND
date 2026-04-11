def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        assert x1 * (y2 - y1) != 0
    return len(coords) >= num_points

def sol():
    return []

assert sat([])
assert not sat([(0, 0)])
assert not sat([(0, 0), (1, 1)])
assert not sat([(0, 0), (1, 0), (2, 1)])
assert not sat([(0, 0), (0, 1)])
assert not sat([(0, 0), (1, 0), (1, 1), (2, 2)])
assert not sat([(0, 0), (1, 1), (1, 2)])
assert not sat([(0, 0), (0, 1), (0, 2)])
assert not sat([(0, 0), (1, 1), (2, 2)])
assert not sat([(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)])
assert not sat([(0, 0), (1, 0), (1, 1), (1, 2), (1,

if __name__ == "__main__":
    assert sat(sol())
