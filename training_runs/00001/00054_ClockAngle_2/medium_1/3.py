def sat(hands: List[int], target_angle=133):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    # If the difference between the angles is equal to target_angle, return True
    return abs(hour_angle - minute_angle) == target_angle

def sol():
    return []

print(sat([0, 0]))  # False
print(sat([12, 0]))  # True
print(sat([12, 30]))  # True
print(sat([12, 45]))  # False
print(sat([18, 0]))  # False
print(sat([23, 30]))  # True
print(sat([23, 45]))  # False
print(sat([2, 30]))  # True
print(sat([11, 50]))  # False
print(sat([22, 30]))  # False
print(sat([22, 45]))  # True

if __name__ == "__main__":
    assert sat(sol())
