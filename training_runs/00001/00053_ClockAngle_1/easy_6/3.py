def sat(hands: Union[int, Tuple[int, int]], target_angle=39) -> bool:
    if isinstance(hands, int):
        h, m = hands, 0
    else:
        h, m = hands
    assert 0 <= h <= 23 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return 0

print(sat(0))  # True
print(sat(39))  # True
print(sat(40))  # False
print(sat(30))  # True
print(sat(59))  # True
print(sat(60))  # False
print(sat(120))  # True
print(sat(180))  # True
print(sat(23.5))  # False
print(sat(59.9))  # False
print(sat(60.1))  # False
print(sat(120.2))  # False
print(sat(180.1))  # False
print(sat(23.4, 45))  # True
print(sat(59.8, 45))  # True
print(sat(60.2, 45))  # False
print(sat(120.3, 45))  # False
print(sat(180.2, 45))  # False

if __name__ == "__main__":
    assert sat(sol())
