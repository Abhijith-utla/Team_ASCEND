def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == target_angle

def sol():
    return [0, 0]

# Test cases
assert sat(sol())
assert not sat([12, 0])
assert not sat([11, 59])
assert not sat([12, 1])
assert not sat([11, 60])

# Checker function
def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == target_angle

if __name__ == "__main__":
    assert sat(sol())
