def sat(hour: int, minute: int) -> bool:
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [120, 360 - 120]

def sol():
    hour, minute = 0, 0
    while True:
        if sat(hour, minute):
            return hour, minute
        minute += 1
        if minute >= 60:
            minute = 0
            hour += 1
            if hour >= 12:
                hour = 0

if __name__ == "__main__":
    assert sat(sol())
