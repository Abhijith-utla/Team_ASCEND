def sat(hour: int, minute: int):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) == 0

def sol():
    return hour, minute

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
