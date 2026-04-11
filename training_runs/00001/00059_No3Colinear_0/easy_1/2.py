def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for i, (x, y) in enumerate(coords):
        assert 0 <= x < side and 0 <= y < side
    return len(coords) == num_points

def sol():
    return []

# Test cases
assert sat([])
assert not sat([(0, 0)])
assert not sat([(5, 5)])
assert sat([(0, 0)], 10, 20)
assert not sat([(0, 0)], 5, 20)
assert not sat([(0, 0)], 10, 19)
assert sat([(0, 0)], 10, 20, True)
assert not sat([(0, 0)], 10, 20, False)
assert sat([(5, 5)], 10, 20)
assert not sat([(5, 5)], 5, 20)
assert not sat([(5, 5)], 10, 19)

if __name__ == "__main__":
    assert sat(sol())
