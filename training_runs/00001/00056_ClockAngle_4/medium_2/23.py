def sat(hour: int, minute: int, target_angle = 68):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return {}

print(sat(0, 0))
print(sat(12, 0))
print(sat(0, 30))
print(sat(12, 30))
print(sat(12, 45))
print(sat(18, 0))
print(sat(23, 55))

if __name__ == "__main__":
    assert sat(sol())
