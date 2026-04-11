def sat(hands: List[int], target_angle=45):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol(hands: List[int], target_angle=45):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

# Test cases
print(sol([0, 0]))  # True
print(sol([12, 0]))  # True
print(sol([12, 30]))  # True
print(sol([12, 31]))  # False
print(sol([1, 30]))  # False
print(sol([1, 31]))  # True
print(sol([1, 0]))  # False
print(sol([11, 59]))  # True
print(sol([11, 0]))  # False

if __name__ == "__main__":
    assert sat(sol())
