def sat(coords: List[List[int]], side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert 0 <= x < side
        assert 0 <= y < side
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

def sol():
    return []

# Incorrect pattern:
def sol(x):
    return []

# Correct pattern:
def sol(coords: List[List[int]], side=1, num_points=1):
    for i in range(len(coords)):
        x, y = coords[i]
        assert 0 <= x < side
        assert 0 <= y < side
    return len({(a, b) for a, b in coords}) == len(coords) >= num_points

# Test case
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
