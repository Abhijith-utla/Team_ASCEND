def sat(hands: List[int], target_angle=68):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

assert sat([])
assert not sat([0, 0])
assert sat([12, 0])
assert not sat([12, 30])
assert not sat([12, 31])
assert sat([11, 59])
assert not sat([13, 0])
assert not sat([23, 0])
assert sat([1, 1])
assert not sat([2, 29])
assert sat([11, 58])
assert not sat([12, 60])
assert not sat([23, 59])

# Do not run this block as it is used for validation
if __name__ == "__main__":
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    assert sat(sol())
