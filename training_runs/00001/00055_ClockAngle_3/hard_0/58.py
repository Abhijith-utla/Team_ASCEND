def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# The function 'sat' does not take any arguments.
# Therefore, 'sol' does not require any arguments.
# But, 'sol' is returning an empty list because there is no logic inside 'sol'.
# Hence, the function 'sol' does not return anything, but does not do anything.

if __name__ == "__main__":
    assert sat(sol())
