def sat(hands):
    h, m = hands
    assert 0 < h < 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m + 1
    return True

def sol():
    return None

if __name__ == "__main__":
    assert sat(sol())
