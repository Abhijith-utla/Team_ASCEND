def sat(coords, side=10, num_points=20):
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        return x1 * (y2 - y1) != 0

def sol():
    return []

# This function is not correct because the function `sat` is not defined.
# The function `sol` is supposed to return an empty list.

if __name__ == "__main__":
    assert sat(sol())
