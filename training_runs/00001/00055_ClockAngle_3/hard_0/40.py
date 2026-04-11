def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

if __name__ == "__main__":
    assert sat([])
    assert not sat([h, m] for h in range(1, 13) for m in range(0, 60))
    assert sat([h, m] for h in range(1, 13) for m in range(0, 60))
    assert sat([12, 0])
    assert sat([12, 30])
    assert sat([12, 45])
    assert not sat([12, 55])
    assert sat([12, 75])
    assert sat([12, 90])
    assert not sat([13, 0])
    assert not sat([13, 45])
    assert sat([1, 1])
    assert sat([1, 30])
    assert sat([1, 45])
    assert not sat([2, 0])
    assert not sat([2, 30])
    assert not sat([2, 45])
    assert

if __name__ == "__main__":
    assert sat(sol())
