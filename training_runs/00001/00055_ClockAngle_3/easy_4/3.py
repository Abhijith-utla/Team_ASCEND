def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == target_angle

def sol():
    return []

# assert sat([12, 0])
# assert not sat([11, 59])
# assert not sat([12, 0])
# assert not sat([13, 0])
# assert not sat([11, 30])
# assert sat([12, 30])
# assert not sat([13, 30])
# assert not sat([13, 45])
# assert not sat([13, 60])
# assert not sat([13, 70])
# assert not sat([13, 85])
# assert not sat([13, 90])
# assert not sat([13, 105])
# assert not sat([13, 120])
# assert not sat([13, 135])
# assert not sat([13, 150])
# assert not sat([13, 165])
# assert not sat([13, 180])
# assert not sat([13, 195

if __name__ == "__main__":
    assert sat(sol())
