def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# Test cases
assert sat([])
assert not sat([3, 30])
assert sat([12, 0])
assert sat([5, 15])
assert not sat([9, 55])
assert not sat([10, 55])

# Checker code
def main():
    hands = [int(i) for i in input().split()]
    if sat(hands):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()

if __name__ == "__main__":
    assert sat(sol())
