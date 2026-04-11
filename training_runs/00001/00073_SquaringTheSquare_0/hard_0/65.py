def sat(xy_sides: List[List[int]]):
    n = max(x + side for x, y, side in xy_sides)
    assert len({side for x, y, side in xy_sides}) == len(xy_sides) > 1
    for x, y, s in xy_sides:
        assert 0 <= y < y + s <= n and 0 <= x
        for x2, y2, s2 in xy_sides:
            assert s2 <= s or x2 >= x + s or x2 + s2 <= x or y2 >= y + s or y2 + s2 <= y

    return sum(side ** 2 for x, y, side in xy_sides) == n ** 2

def sol():
    return [1, 1]

assert sat([[1, 1, 1]])
assert not sat([[2, 2, 2]])
assert sat([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
assert not sat([[1, 1, 1], [3, 3, 3], [4, 4, 4]])

if __name__ == "__main__":
    assert sat(sol())
