def sat(coords, side=10, num_points=20):
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        return len(coords) >= num_points

def sol():
    return []

# This is an example of a solution. It returns an empty list.
# You may replace this with any valid answer object.

if __name__ == "__main__":
    assert sat(sol())
