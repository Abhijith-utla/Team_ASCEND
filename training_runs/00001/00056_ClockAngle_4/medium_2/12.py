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
assert sat(0, 60)
assert not sat(12, 60)
assert sat(1, 20)
assert not sat(12, 20)
assert not sat(6, 70)
assert sat(6, 70)
assert sat(5, 58)
assert not sat(5, 59)
assert sat(11, 30)
assert not sat(11, 31)
assert sat(11, 59)
assert not sat(12, 0)
assert sat(23, 0)

if __name__ == "__main__":
    assert sat(sol())
