def sat(xy_sides):
    max_sum = max(x + side for x, y, side in xy_sides)
    assert len({side for x, y, side in xy_sides}) == len(xy_sides) > 1
    for x, y, s in xy_sides:
        assert 0 <= y <= max_sum and 0 <= x
        for x2, y2, s2 in xy_sides:
            assert s2 <= x
    return sum(side ** 2 for x, y, side in xy_sides) == max_sum ** 2

def sol():
    return {
        "x": 0,
        "y": 0,
        "sum_of_sides": 0,
        "sum_of_squares": 0,
    }

if __name__ == "__main__":
    assert sat(sol())
