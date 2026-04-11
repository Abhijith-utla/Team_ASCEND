def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# Test cases
print(sat([12, 0])) # True
print(sat([12, 30])) # True
print(sat([12, 45])) # True
print(sat([0, 0])) # True
print(sat([12, 45])) # False
print(sat([11, 55])) # False
print(sat([13, 0])) # False
print(sat([0, 55])) # False

if __name__ == "__main__":
    assert sat(sol())
