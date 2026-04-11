def sat(coords, side=10, num_points=20):
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        return len(coords) >= num_points

def sol():
    return []

# Assuming that the 'coords' variable is a list of tuples (x, y)
# for example: coords = [(0, 0), (1, 1), (2, 2)]

assert sat(coords)

if __name__ == "__main__":
    assert sat(sol())
