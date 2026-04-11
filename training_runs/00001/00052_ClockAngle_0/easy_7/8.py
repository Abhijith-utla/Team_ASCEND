def sat(hands: Tuple[int, int]) -> bool:
    h, m = hands
    assert 0 <= h < 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 12
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [0, 60, 360]

def sol():
    return (12, 30)

# Test case
assert sat(sol())
!python -m doctest -v test.py

if __name__ == "__main__":
    assert sat(sol())
