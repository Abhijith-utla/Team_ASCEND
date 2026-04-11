def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for i, (x1, y1) in enumerate(coords):
        assert 0 <= x1 < side and 0 <= y1 < side
    return len(coords) > num_points

def sol():
    return []

# Test cases
print(sat([(5, 5), (5, 6), (6, 6)]))  # False
print(sat([(5, 5), (5, 6), (6, 5)]))  # False
print(sat([(5, 5), (5, 6), (6, 6), (7, 7)]))  # True
print(sat([(5, 5), (5, 6), (6, 6)]))  # True

if __name__ == "__main__":
    assert sat(sol())
