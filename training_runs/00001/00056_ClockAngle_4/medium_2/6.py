def sat(hour: int, minute: int, target_angle = 68):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return None

assert sat(3, 0)
assert not sat(12, 0)
assert sat(12, 30)
assert not sat(11, 45)
assert sat(11, 15)
assert not sat(23, 30)

if __name__ == "__main__":
    assert sat(sol())
