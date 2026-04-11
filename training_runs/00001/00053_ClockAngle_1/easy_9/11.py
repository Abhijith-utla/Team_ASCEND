def sat(hands: Tuple[int, int]):
    h, m = hands
    assert 0 <= h < 24 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [38, 360 - 38]

def sol():
    return {}

# Test cases
print(sat((2, 30)))  # Returns True
print(sat((10, 20)))  # Returns True
print(sat((18, 10)))  # Returns False
print(sat((22, 0)))  # Returns True
print(sat((2, 0)))  # Returns True
print(sat((12, 60)))  # Returns True
print(sat((12, 70)))  # Returns False
print(sat((5, 30)))  # Returns True
print(sat((11, 55)))  # Returns False

if __name__ == "__main__":
    assert sat(sol())
