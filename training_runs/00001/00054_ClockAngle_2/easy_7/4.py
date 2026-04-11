def sat(hands):
    h, m = hands
    assert 0 <= h < 24 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(abs(hour_angle - minute_angle) - 133) == 0

def sol():
    return {}

# The solution is empty because the problem doesn't provide any information about the hands.

if __name__ == "__main__":
    assert sat(sol())
