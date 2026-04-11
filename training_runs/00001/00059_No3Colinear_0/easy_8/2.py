def sat(coords, side=10, num_points=20):
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        return x1 * (y2 - y1) != 0

def sol():
    import itertools

    def is_straight_line(coords, side=10, num_points=20):
        for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
            if x1 * (y2 - y1) == 0:
                return False
        return True

    return is_straight_line()

# Test
print(sat([(1,1), (2,2), (3,3), (4,4)]))

if __name__ == "__main__":
    assert sat(sol())
