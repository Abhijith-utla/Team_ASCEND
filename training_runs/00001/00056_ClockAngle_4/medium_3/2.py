def sat(hour: int, minute: int):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [180, 360 - 180]

def sol():
    for hour in range(1, 13):  # 12 hours
        for minute in range(0, 60):  # 60 minutes
            if sat(hour, minute):
                return hour, minute
    return None

print(sol())

if __name__ == "__main__":
    assert sat(sol())
