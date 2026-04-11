def sat(hands: Tuple[int, int]) -> bool:
    h, m = hands
    assert 0 <= h < 24 and 0 <= m < 60
    hour_angle = 30 * h + m
    minute_angle = 6 * m
    return hour_angle != minute_angle

def sol():
    return ()

def test():
    assert sol() == ()

test()

if __name__ == "__main__":
    assert sat(sol())
