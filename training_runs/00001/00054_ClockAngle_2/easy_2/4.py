def sat(hands: List[int], target_angle: float = 133) -> bool:
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == target_angle

def sol():
    return []

# Test cases
assert not sat([])
assert not sat([5, 0])
assert sat([12, 30])
assert not sat([12, 60])
assert sat([11, 55])
assert not sat([12, 0])

# Final check
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
