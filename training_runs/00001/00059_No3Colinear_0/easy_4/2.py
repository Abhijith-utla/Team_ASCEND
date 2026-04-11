def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for i, (x1, y1) in enumerate(coords):
        assert 0 <= x1 < side and 0 <= y1 < side
    return len(coords) >= num_points

def sol():
    return []

# If we were to implement the solution, the function would look something like this
def sol(coords: List[Tuple[int, int]], side=10, num_points=20):
    for i, (x1, y1) in enumerate(coords):
        assert 0 <= x1 < side and 0 <= y1 < side
    return len(coords) >= num_points

# Testing
assert sat(sol())
!sat(sol(coords=[(5, 5), (6, 6)]))
!sat(sol(coords=[(5, 5), (6, 7)]))

if __name__ == "__main__":
    assert sat(sol())
