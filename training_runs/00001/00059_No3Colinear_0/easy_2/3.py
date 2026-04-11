def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for i, (x, y) in enumerate(coords):
        assert 0 <= x < side and 0 <= y < side
    return len(coords) == num_points-1

def sol():
    return []

# Test cases
assert sat(coords=[(0, 0)]) == False
assert sat(coords=[(5, 5)]) == False
assert sat(coords=[(0, 0), (5, 5)]) == False
assert sat(coords=[(0, 0), (2, 2)]) == True
assert sat(coords=[(0, 0), (5, 5), (2, 2)]) == True
assert sat(coords=[(0, 0), (5, 5), (7, 7)]) == False

if __name__ == "__main__":
    assert sat(sol())
