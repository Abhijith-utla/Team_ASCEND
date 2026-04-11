def sat(coords, side=2, num_points=4):
    for i1 in range(len(coords)):
        x1, y1 = coords[i1]
        assert 0 <= x1 < side, "x1 out of range"
        for i2 in range(i1):
            x2, y2 = coords[i2]
            for i3 in range(i2):
                x3, y3 = coords[i3]
                if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
                    return True
    return len({(a, b) for a, b in coords}) >= num_points

def sol():
    return {}

# This is an example of a valid solution.
# Replace the return value with your actual solution.
def sol():
    return {(1, 2), (3, 4), (5, 6), (7, 8)}

if __name__ == "__main__":
    assert sat(sol())
