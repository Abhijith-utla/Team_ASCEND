def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

print(sat([0, 0]))
print(sat([12, 0]))
print(sat([12, 30]))
print(sat([12, 60]))
print(sat([11, 59]))
print(sat([138, 0]))
print(sat([138, 59]))
print(sat([138, 1]))
print(sat([138, 58]))
print(sat([2, 0]))
print(sat([2, 30]))
print(sat([2, 45]))
print(sat([2, 60]))
print(sat([1, 59]))

if __name__ == "__main__":
    assert sat(sol())
