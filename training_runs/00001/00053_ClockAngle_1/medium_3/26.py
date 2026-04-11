def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 <= h < 24 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return [], []

# Test cases:
assert sat(sol()) == (0, 0)
assert sat(sol([12, 0])) == (0, 0)
assert sat(sol([12, 30])) == (180, 0)
assert sat(sol([23, 0])) == (0, 0)
assert sat(sol([23, 30])) == (90, 0)
assert sat(sol([1, 30])) == (180, 0)
assert sat(sol([11, 30])) == (180, 0)
assert sat(sol([22, 45])) == (67.5, 0)
assert sat(sol([2, 40])) == (60, 0)
assert sat(sol([10, 55])) == (25, 0)
assert sat(sol([7, 15])) == (90, 0)
assert sat(sol([21, 50])) == (125, 0

if __name__ == "__main__":
    assert sat(sol())
