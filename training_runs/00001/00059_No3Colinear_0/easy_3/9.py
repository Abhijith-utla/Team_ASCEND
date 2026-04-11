def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for i, (x, y) in enumerate(coords):
        assert 0 <= x < side and 0 <= y < side
    return len(coords) == num_points+1

def sol():
    return []

# Test cases
coords_test_1 = [(5, 5), (10, 10), (15, 15)]
coords_test_2 = [(5, 5), (10, 10), (15, 15), (20, 20)]
assert sat(coords_test_1)
assert not sat(coords_test_2)

if __name__ == "__main__":
    assert sat(sol())
