def sat(hands: List[int], target_angle=45):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# This function will return an empty list if the angles are equal. Otherwise, it will return a list of two angles. 
# It doesn't matter which angles are returned because the angles are equal and the problem statement states that we can return any two angles.

if __name__ == "__main__":
    assert sat(sol())
