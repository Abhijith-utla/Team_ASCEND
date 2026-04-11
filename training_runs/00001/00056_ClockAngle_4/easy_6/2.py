def sat(hour: int, minute: int) -> bool:
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [90, 360 - 90]

def sol():
    return 0, 0

if __name__ == "__main__":
    assert sat(sol())
