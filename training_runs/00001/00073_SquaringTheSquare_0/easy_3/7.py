def sat(xy_sides):
    max_sum = max((x * 2) + side for x, y, side in xy_sides)
    assert len({side for x, y, side in xy_sides}) == len(xy_sides) > 1
    for x, y, s in xy_sides:
        assert 0 <= y < y + s <= max_sum and 0 <= x
        for x2, y2, s2 in xy_sides:
            assert not (s2 <= s or x2 >= x + s or x2 + s2 <= x or y2 >= y + s or y2 + s2 <= y)
    return sum(side ** 2 for x, y, side in xy_sides) == max_sum ** 2

def sol():
    return [(1,1,1)]

if __name__ == "__main__":
    assert sat(sol())
