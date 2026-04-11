def sat(hour: int, minute: int) -> bool:
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [90, 360 - 90]

def sol():
    for hour in range(12):
        for minute in range(0, 60, 15):
            if sat(hour, minute):
                return hour, minute
    return None

print(f"Hour: {sol()[0]}, Minute: {sol()[1]}")

if __name__ == "__main__":
    assert sat(sol())
