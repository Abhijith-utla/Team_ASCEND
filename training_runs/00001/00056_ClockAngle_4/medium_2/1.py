def sat(hour: int, minute: int, target_angle = 68):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    for hour in range(12):
        for minute in range(60):
            if sat(hour, minute):
                return hour, minute
    return None

# assert sat(0, 0)
# assert sat(12, 0)
# assert sat(12, 30)
# assert sat(12, 60)
# assert sat(18, 0)
# assert sat(18, 30)
# assert sat(23, 30)
# assert sat(23, 45)
# assert sat(23, 59)

if __name__ == "__main__":
    assert sat(sol())
