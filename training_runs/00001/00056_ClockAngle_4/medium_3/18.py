def sat(hour: int, minute: int):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [180, 360 - 180]

def sol():
    hour = 12
    minute = 0
    while True:
        if sat(hour, minute):
            return {"hour": hour, "minute": minute}
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
            if hour == 13:
                hour = 1

if __name__ == "__main__":
    assert sat(sol())
