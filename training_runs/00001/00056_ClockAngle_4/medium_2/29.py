def sat(hour: int, minute: int, target_angle = 68):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return 0, 0

assert sat(0, 0)
assert not sat(12, 0)
assert not sat(0, 30)
assert sat(12, 30)
assert not sat(12, 45)
assert sat(12, 45)
assert not sat(23, 0)
assert not sat(23, 30)
assert not sat(23, 45)
assert not sat(24, 0)
assert not sat(24, 30)
assert not sat(24, 45)
assert not sat(0, 60)
assert not sat(12, 60)
assert not sat(24, 60)

if __name__ == "__main__":
    assert sat(sol())
