def sat(coords, side=10, num_points=20):
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        return len(coords) >= num_points

def sol():
    import random
    import itertools

    def is_valid(coords, side=10, num_points=20):
        for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
            return len(coords) >= num_points

    coords = [(random.randint(0, side), random.randint(0, side)) for _ in range(20)]
    while not is_valid(coords, side, num_points):
        coords = [(random.randint(0, side), random.randint(0, side)) for _ in range(20)]

    return coords

print(sol())

if __name__ == "__main__":
    assert sat(sol())
