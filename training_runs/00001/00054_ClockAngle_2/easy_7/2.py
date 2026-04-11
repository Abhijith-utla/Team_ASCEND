def sat(hands):
    h, m = hands
    assert 0 <= h < 24 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(abs(hour_angle - minute_angle) - 133) == 0

def sol():
    return (0, 0)

# Run the assertion
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
