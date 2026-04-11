def sat(hands: Tuple[int, int], target_angle=133) -> bool:
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == target_angle

def sol():
    return ()

# You may modify this function to solve the problem
def sol(hands: Tuple[int, int], target_angle=133) -> bool:
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == target_angle

# You may add your own assertions to ensure the function works correctly
assert sat((1, 30))
assert not sat((1, 31))
assert sat((12, 0))
assert not sat((12, 1))
assert sat((6, 30))
assert not sat((6, 31))

if __name__ == "__main__":
    assert sat(sol())
