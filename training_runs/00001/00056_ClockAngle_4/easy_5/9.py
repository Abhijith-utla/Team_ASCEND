def sat(hour: int, minute: int) -> bool:
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [120, 360 - 120]

def sol():
    return 0, 0

# Test cases
assert sat(0, 0)
assert not sat(12, 0)
assert not sat(0, 12)
assert sat(6, 30)
assert not sat(1, 31)
assert not sat(11, 59)
assert sat(11, 0)
assert not sat(12, 15)
assert sat(2, 45)
assert not sat(1, 45)
assert not sat(12, 45)
assert sat(12, 0)

if __name__ == "__main__":
    assert sat(sol())
