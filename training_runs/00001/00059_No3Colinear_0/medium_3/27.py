def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        assert x1 * (y2 - y1) != 0
    return len(coords) >= num_points

def sol():
    return []

def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        assert (x2 - y1) * x1 != 0
    return len(coords) >= num_points

# Test cases

# Test case 1
coords = [(0,0), (0,1), (1,0)]
print(sat(coords))  # True

# Test case 2
coords = [(0,0), (0,2), (1,0)]
print(sat(coords))  # False

# Test case 3
coords = [(0,0), (0,3), (1,0)]
print(sat(coords))  # True

# Test case 4
coords = [(0,

if __name__ == "__main__":
    assert sat(sol())
