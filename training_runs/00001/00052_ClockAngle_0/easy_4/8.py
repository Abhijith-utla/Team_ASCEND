def sat(hands):
    h, m = hands
    assert 0 < h < 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return True

def sol():
    for h in range(1, 12):
        for m in range(0, 60):
            if sat(h, m):
                return h, m
    return None

# Test the function
if __name__ == "__main__":
    assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
