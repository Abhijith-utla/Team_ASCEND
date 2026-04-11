def sat(hour: int, minute: int):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) == 180

def sol():
    return None

assert sat(3, 0)
assert sat(12, 0)
assert not sat(6, 0)
assert sat(12, 30)
assert not sat(3, 30)
assert not sat(6, 30)
assert not sat(3, 45)
assert sat(2, 45)
assert not sat(11, 45)
assert sat(11, 15)
assert not sat(2, 15)
assert not sat(12, 15)
assert sat(12, 45)
assert not sat(1, 45)
assert not sat(12, 55)

if __name__ == "__main__":
    assert sat(sol())
