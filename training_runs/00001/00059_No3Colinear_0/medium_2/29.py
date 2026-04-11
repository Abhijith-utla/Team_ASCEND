def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for i, (x1, y1) in enumerate(coords):
        assert 0 <= x1 < side and 0 <= y1 < side
        for (x2, y2) in coords[i+1:]:
            assert x1 * (y2 - y1) != 0
    return len(coords) >= num_points

def sol():
    return []

# This function is not used in the solution, it's just a placeholder.
def not_used(coords, side=10, num_points=20):
    return []

# This function is not used in the solution, it's just a placeholder.
def not_used2(coords, side=10, num_points=20):
    return []

# This function is not used in the solution, it's just a placeholder.
def not_used3(coords, side=10, num_points=20):
    return []

# This function is not used in the solution, it's just a placeholder.
def not_used4(coords, side=10, num_points=20):
    return []

# This function is not used in the solution, it's just a placeholder.
def not_used5(coords, side=10, num_points=20):
    return []

# This function is not used in the solution, it's just a placeholder.
def not_used6

if __name__ == "__main__":
    assert sat(sol())
