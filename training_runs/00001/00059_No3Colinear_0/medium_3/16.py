def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        assert x1 * (y2 - y1) != 0
    return len(coords) >= num_points

def sol():
    return []

# Test case 1: Normal case
# coords = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
# assert sat(coords)

# Test case 2: Side case
# coords = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (3, 4), (4, 3), (4, 4)]
# assert sat(coords, side=5)

# Test case 3: Multiple points case
# coords = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]
# assert sat(coords, num_points=10)

# Test case 4: Case where there is no solution
# coords = [(1,

if __name__ == "__main__":
    assert sat(sol())
