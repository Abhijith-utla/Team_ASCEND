def sat(hour: int, minute: int):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) == 180

def sol():
    for hour in range(12):
        for minute in range(60):
            if sat(hour, minute):
                return hour, minute
    return None

# Test
hour, minute = sol()
if sat(hour, minute):
    print(f"The angles are exactly 180 degrees apart at {hour}:{minute:02d}")
else:
    print(f"The angles are not exactly 180 degrees apart at {hour}:{minute:02d}")

if __name__ == "__main__":
    assert sat(sol())
