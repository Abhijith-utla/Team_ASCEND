def sat(coords: List[Tuple[int, int]], side=10, num_points=20):
    for i1, (x1, y1) in enumerate(coords):
        assert 0 <= x1 < side and 0 <= y1 < side
        for i2, (x2, y2) in enumerate(coords):
            if i1 != i2:
                for i3, (x3, y3) in enumerate(coords):
                    if i2 != i3 and i1 != i3:
                        assert (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) != 0
    return len(coords) == num_points

def sol():
    return []

# This is a placeholder for the actual solution.
# The actual solution will depend on the specific problem and the constraints.
# For example, if the problem is to find a point on a circle, the solution could be:

def sol():
    return [(5, 5)]

# This is a placeholder for the actual solution.
# The actual solution will depend on the specific problem and the constraints.
# For example, if the problem is to find a point on a square, the solution could be:

def sol():
    return [(0, 0), (10, 0), (10, 10), (0, 10)]

# This is a placeholder for the actual solution.
# The actual solution will depend on the specific problem and the constraints.
# For example, if the problem is to find a point on a triangle, the solution could be:

def sol():
    return [(0, 0), (5, 0), (5, 5)]

# This is a placeholder for the actual solution.
# The actual solution will depend on the specific problem

if __name__ == "__main__":
    assert sat(sol())
