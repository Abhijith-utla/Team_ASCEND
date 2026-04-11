def sat(hands: List[int], target_angle=133):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    # If the difference between the absolute difference of the angles is equal to target_angle, return True
    return abs(abs(hour_angle - minute_angle) - target_angle) == 0

def sol():
    return []

# assert sat([])
# assert not sat([5, 5])
# assert not sat([11, 30])
# assert sat([1, 30])
# assert not sat([12, 0])
# assert sat([12, 15])
# assert not sat([0, 0])
# assert sat([6, 60])
# assert not sat([13, 30])
# assert not sat([11, 35])
# assert not sat([11, 55])
# assert sat([1, 55])
# assert not sat([12, 55])
# assert not sat([0, 55])
# assert not sat([2, 5])
# assert not sat([1, 60])
# assert not sat([12, 60])
# assert sat([1, 0])
# assert not sat([13, 0])
# assert not sat([1, 35])
# assert not sat([1, 45])
# assert

if __name__ == "__main__":
    assert sat(sol())
