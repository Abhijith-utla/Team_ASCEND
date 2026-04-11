def sat(coords, side=10, num_points=20):
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        return len(coords) >= num_points

def sol():
    return []

Incorrect pattern:
def sol(x):
    ...

if __name__ == "__main__":
    assert sat(sol())
