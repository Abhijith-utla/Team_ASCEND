def sat(hands: Tuple[int, int]) -> bool:
    h, m = hands
    assert 0 <= h < 24 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return ()

# Test cases
print(sat((12, 30)))  # True
print(sat((12, 45)))  # False
print(sat((2, 15)))  # True
print(sat((11, 59)))  # False
print(sat((0, 0)))  # True
print(sat((1, 1)))  # False
print(sat((23, 59)))  # True
print(sat((18, 30)))  # False

if __name__ == "__main__":
    assert sat(sol())
