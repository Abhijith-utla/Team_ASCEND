def sat(hour: int, minute: int, target_angle = 68):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return 0, 0

assert sat(0, 0)
assert not sat(12, 0)
assert not sat(0, 30)
assert sat(6, 30)
assert not sat(11, 59)
assert sat(11, 58)
assert not sat(23, 1)

if __name__ == "__main__":
    assert sat(sol())
