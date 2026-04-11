def sat(hands: List[int], target_angle=68):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# Test cases
print(sat([0, 0]))  # False
print(sat([12, 0]))  # False
print(sat([12, 30]))  # True
print(sat([12, 35]))  # False
print(sat([3, 0]))  # False
print(sat([3, 30]))  # False
print(sat([3, 45]))  # False
print(sat([11, 55]))  # True
print(sat([11, 30]))  # False

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
