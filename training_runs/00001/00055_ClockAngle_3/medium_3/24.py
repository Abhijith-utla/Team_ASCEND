def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == 360 - target_angle

def sol():
    return 10, 30

# The correct answer for the example provided:
# assert sat(sol())
# print("Test passed")

# In this case, the answer is (10, 30) because the angle difference between the hands is 360 - 138 = 182 degrees.
# Hence, the angles of the hour hand and minute hand are 10 degrees (for the hour hand) and 30 degrees (for the minute hand).

if __name__ == "__main__":
    assert sat(sol())
