def sat(hour: int, minute: int) -> bool:
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [120, 360 - 120]

def sol():
    return {}

assert sat(3, 0)
assert not sat(6, 0)
assert sat(12, 0)
assert not sat(2, 30)
assert not sat(2, 45)
assert sat(2, 15)
assert not sat(11, 55)
assert sat(11, 0)

if __name__ == "__main__":
    assert sat(sol())
