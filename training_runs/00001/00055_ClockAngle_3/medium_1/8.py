def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return hour_angle == minute_angle

def sol():
    return None

# Uncomment the following lines to test the function
# assert sat([4, 0])
# assert not sat([12, 30])
# assert not sat([11, 59])
# assert not sat([12, 0])
# assert not sat([13, 0])
# assert sat([1, 1])
# assert not sat([1, 1])
# assert not sat([2, 1])
# assert not sat([3, 1])
# assert not sat([4, 1])
# assert not sat([5, 1])
# assert not sat([6, 1])
# assert not sat([7, 1])
# assert not sat([8, 1])
# assert not sat([9, 1])
# assert not sat([10, 1])
# assert not sat([11, 1])
# assert not sat([12, 1])
# assert sat([1, 59])
# assert not sat([2, 59])
# assert not sat([3,

if __name__ == "__main__":
    assert sat(sol())
