def sat(hour: int, minute: int):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) == 180

def sol():
    hour = 0
    minute = 0
    while not sat(hour, minute):
        if hour == 12:
            hour = 0
        else:
            hour += 1
        minute = 0
        while minute < 60:
            if sat(hour, minute):
                return hour, minute
            else:
                minute += 1

if __name__ == "__main__":
    assert sat(sol())
