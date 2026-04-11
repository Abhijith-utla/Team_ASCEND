def sat(hands):
    h, m = hands
    assert 0 < h < 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return False

def sol():
    return {}

def sat(hands):
    h, m = hands
    assert 0 < h < 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return (hour_angle, minute_angle)

if __name__ == "__main__":
    hands = sol()
    assert sat(hands)

# Testing
def test_sol():
    assert sol() == {}

def test_sat():
    assert sat((4, 30)) == (105, 18)
    assert sat((12, 0)) == (360, 0)
    assert sat((11, 55)) == (90, 30)
    assert sat((1, 60)) == (30, 60)

test_sol()
test_sat()

if __name__ == "__main__":
    assert sat(sol())
