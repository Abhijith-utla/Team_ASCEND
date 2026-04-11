def sat(hour: int, minute: int):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) == 360

def sol():
    return None

# Checker
assert sat(0, 0)
assert not sat(12, 00)
assert sat(12, 30)
assert not sat(2, 30)
assert sat(2, 15)
assert not sat(3, 15)
assert sat(4, 15)
assert not sat(5, 15)
assert sat(6, 15)
assert not sat(7, 15)
assert sat(8, 15)
assert not sat(9, 15)
assert sat(10, 15)
assert not sat(11, 15)
assert sat(12, 15)
assert not sat(13, 15)
assert sat(14, 15)
assert not sat(15, 15)
assert sat(16, 15)
assert not sat(17, 15)
assert sat(18, 15)
assert not sat(19, 15)
assert

if __name__ == "__main__":
    assert sat(sol())
