def sat(hands: List[int], target_angle=45):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# assert sat([])
# assert sat([3, 30])
# assert sat([12, 0])
# assert not sat([12, 15])
# assert sat([12, 15])
# assert not sat([12, 45])
# assert sat([12, 45])
# assert not sat([1, 30])
# assert sat([1, 30])
# assert not sat([0, 30])
# assert sat([0, 30])
# assert not sat([11, 55])
# assert sat([11, 55])
# assert not sat([11, 60])
# assert sat([11, 60])

# assert sat([2, 30])
# assert sat([3, 30])
# assert sat([4, 30])
# assert sat([5, 30])
# assert sat([6, 30])
# assert sat([7, 30])
# assert sat([8

if __name__ == "__main__":
    assert sat(sol())
