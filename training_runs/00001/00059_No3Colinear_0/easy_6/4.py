def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for i, (x1, y1) in enumerate(coords):
        assert 0 <= x1 < side and 0 <= y1 < side
    return len(coords) > num_points

def sol():
    return []

# Example usage:
print(sat([(5, 5), (10, 10), (15, 15)], 20, 20))  # True
print(sat([(5, 5), (10, 10), (15, 15)], 20, 19))  # False

if __name__ == "__main__":
    assert sat(sol())
