def sat(hour: int, minute: int):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) == 0

def sol():
    return 0, 0

assert sat(sol()[0], sol()[1])

if __name__ == "__main__":
    assert sat(sol())
