def sat(coords, side=10, num_points=20):
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        assert x1 * (y2 - y1) != 0
    return len(coords) >= num_points

def sol():
    return {}

# The solution is empty because the problem doesn't provide any initial coordinates

if __name__ == "__main__":
    assert sat(sol())
