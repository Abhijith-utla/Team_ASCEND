def sat(hands):
    h, m = hands
    assert 0 <= h < 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(abs(hour_angle - minute_angle) - 133) == 0

def sol():
    h, m = 0, 0
    while True:
        if sat(h, m):
            return h, m
        m += 1
        if m == 60:
            h += 1
            m = 0
        if h == 12:
            h = 0

if __name__ == "__main__":
    assert sat(sol())
