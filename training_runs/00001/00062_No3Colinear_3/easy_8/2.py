def sat(coords: List[Tuple[int, int]], side=2, num_points=4):
    for i1, (x1, y1) in enumerate(coords):
        assert 0 <= x1 < side and 0 <= y1 < side
        for x2, y2 in coords[i1+1:]:
            for x3, y3 in coords[i1+2:]:
                if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
                    return False
    return len(set(coords)) == num_points

def sol():
    return []

# Adding a random set of points
def sol_with_points(coords=[(2, 3), (5, 6), (7, 8), (1, 2)]):
    return coords

# Adding a diagonal line to the set of points
def sol_with_diagonal_line(coords=[(2, 3), (5, 6), (7, 8), (9, 1)]):
    return coords

# Adding a vertical line to the set of points
def sol_with_vertical_line(coords=[(2, 3), (5, 6), (7, 8), (10, 9)]):
    return coords

# Adding a horizontal line to the set of points
def sol_with_horizontal_line(coords=[(2, 3), (5, 6), (7, 9), (11, 8)]):
    return coords

# Adding a line that isn't a diagonal, vertical, or horizontal line to the set of points
def sol

if __name__ == "__main__":
    assert sat(sol())
