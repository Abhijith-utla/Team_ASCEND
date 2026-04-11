def sat(xy_sides):
    max_sum = max(x + side for x, y, side in xy_sides)
    assert len({side for x, y, side in xy_sides}) == len(xy_sides) > 1
    for x, y, s in xy_sides:
        assert 0 <= y <= max_sum and 0 <= x
        for x2, y2, s2 in xy_sides:
            assert s2 <= s or x2 >= x + s or x2 + s2 <= x or y2 >= y + s or y2 + s2 <= y
    return sum(side ** 2 for x, y, side in xy_sides) == max_sum ** 2

def sol():
    return (0, 0, 0)

# Test cases
assert sat(sol())
assert sat((1, 1, 1))
assert not sat((1, 2, 1))
assert not sat((3, 4, 5))
assert not sat((2, 2, 3))
assert not sat((1, 2, 3))
assert not sat((2, 2, 2))
assert not sat((3, 3, 3))
assert not sat((4, 4, 4))
assert not sat((1, 3, 4))
assert not sat((5, 6, 7))
assert not sat((6, 7, 8))
assert not sat((7, 8, 9))
assert not sat((8, 9, 10))
assert not sat((9, 10, 11))
assert not sat((10, 11, 12))
assert not sat((11, 12, 13))
assert not sat((12, 13, 1

if __name__ == "__main__":
    assert sat(sol())
