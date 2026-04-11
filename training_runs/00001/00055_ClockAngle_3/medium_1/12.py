def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return hour_angle == minute_angle

def sol():
    return []

if __name__ == "__main__":
    print(sat([0, 0]))  # True
    print(sat([12, 0]))  # True
    print(sat([12, 30]))  # True
    print(sat([12, 45]))  # False
    print(sat([1, 0]))  # True
    print(sat([1, 30]))  # False
    print(sat([2, 0]))  # True
    print(sat([23, 0]))  # False
    print(sat([11, 30]))  # True
    print(sat([11, 45]))  # False

if __name__ == "__main__":
    assert sat(sol())
