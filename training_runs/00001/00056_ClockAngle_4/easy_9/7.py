def sat(hour: int, minute: int):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) == 0

def sol():
    return {}

assert sat(0, 0)
assert sat(12, 0)
assert sat(6, 0)
assert not sat(7, 30)
assert not sat(16, 30)
assert sat(2, 30)
assert not sat(23, 30)
assert not sat(1, 60)
assert not sat(6, 60)
assert sat(12, 15)
assert not sat(11, 70)
assert not sat(22, 45)
assert sat(3, 15)
assert not sat(30, 5)
assert not sat(23, 70)
assert not sat(12, 80)
assert not sat(14, 0)
assert not sat(18, 30)
assert not sat(22, 0)

if __name__ == "__main__":
    assert sat(sol())
