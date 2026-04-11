def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 <= h <= 23 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return [0, 0]

# Testing the solution
print(sat(sol()))  # This should return [0, 0]

# You can manually test the solution by changing the parameters
print(sat([h, m]))  # Replace h and m with different values

if __name__ == "__main__":
    assert sat(sol())
