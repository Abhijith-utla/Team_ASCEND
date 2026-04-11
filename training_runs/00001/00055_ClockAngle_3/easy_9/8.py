def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == 360 - target_angle

def sol():
    return {"hands": [0, 0]}

assert sat(sol()["hands"])

# test with different hands
assert not sat(sol()["hands"])
assert not sat(sol()["hands"])
assert sat(sol()["hands"])

# test with different minutes
assert not sat(sol()["hands"])
assert not sat(sol()["hands"])
assert not sat(sol()["hands"])
assert sat(sol()["hands"])

# test with different hours
assert not sat(sol()["hands"])
assert not sat(sol()["hands"])
assert not sat(sol()["hands"])
assert sat(sol()["hands"])

if __name__ == "__main__":
    assert sat(sol())
