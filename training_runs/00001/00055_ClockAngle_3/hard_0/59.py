def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# Testing code
# assert sat([0, 0])
# assert not sat([12, 0])
# assert not sat([11, 59])
# assert sat([11, 30])
# assert not sat([11, 45])
# assert sat([12, 15])
# assert not sat([1, 15])
# assert sat([1, 30])
# assert not sat([1, 45])
# assert sat([2, 0])
# assert not sat([11, 60])
# assert sat([12, 30])
# assert not sat([13, 0])
# assert sat([13, 30])
# assert not sat([13, 45])
# assert sat([1, 59])
# assert not sat([2, 1])
# assert sat([2, 30])
# assert not sat([2, 45])
# assert sat([3, 0])
# assert not sat([11,

if __name__ == "__main__":
    assert sat(sol())
