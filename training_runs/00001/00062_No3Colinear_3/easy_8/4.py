def sat(coords: List[Tuple[int, int]], side=2, num_points=4):
    for i1, (x1, y1) in enumerate(coords):
        assert 0 <= x1 < side and 0 <= y1 < side
        for x2, y2 in coords[i1+1:]:
            for x3, y3 in coords[i1+2:]:
                if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
                    return False
    return len(set(coords)) == num_points

def sol():
    return {}

# This solution has two parts:
# 1. We need to find the coordinates of the corners of the rectangle where the points will be.
# 2. We need to check whether these corners form a square.

# First, let's find the corners of the rectangle.
# The rectangle is a square if and only if all points have the same x-coordinate.
# We know that the x-coordinates of the points are 0, side-1, 0, side-1, so we can say that the rectangle's corners are (0, 0), (0, side-1), (side-1, 0), (side-1, side-1)

corners = [(0, 0), (0, 2), (2, 0), (2, 2)]

# Now, we need to check whether the rectangle's corners form a square.
# A rectangle can be a square if and only if it has the same y-coordinate for all its corners.
# We know that the y-coordinates of the corners are 0, 2, 0

if __name__ == "__main__":
    assert sat(sol())
