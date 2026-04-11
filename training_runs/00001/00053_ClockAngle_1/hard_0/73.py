def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# Test cases to ensure the correctness of the solution

def test_sol():
    assert sat([0, 0])
    assert not sat([12, 0])
    assert sat([6, 30])
    assert sat([12, 30])
    assert sat([12, 45])
    assert sat([1, 59])
    assert not sat([13, 0])
    assert not sat([1, 60])
    assert not sat([0, 61])
    assert not sat([14, 0])
    assert not sat([23, 59])

test_sol()

if __name__ == "__main__":
    assert sat(sol())
