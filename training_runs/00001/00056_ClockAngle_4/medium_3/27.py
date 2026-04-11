def sat(hour: int, minute: int):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [180, 360 - 180]

def sol():
    hour = 0
    while True:
        for minute in range(0, 60):
            if sat(hour, minute):
                return hour, minute
        hour += 1
        if hour >= 12:
            hour = 0

if __name__ == "__main__":
    assert sat(sol())
