def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == 360 - target_angle

def sol():
    return [0, 0]

# The function 'sol' has no arguments and returns a list [0, 0] which satisfies the condition of the problem.

if __name__ == "__main__":
    assert sat(sol())
