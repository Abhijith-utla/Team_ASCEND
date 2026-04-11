def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return [], 0

# Test cases
print(sat([3, 0]))
print(sat([11, 0]))
print(sat([11, 30]))
print(sat([12, 0]))
print(sat([12, 30]))
print(sat([0, 0]))
print(sat([0, 30]))

# Correct answer
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
