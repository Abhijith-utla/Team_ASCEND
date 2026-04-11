def sat(hour: int, minute: int, target_angle = 68):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return hour, minute

hour, minute = 0, 0  # replace with correct values
while not sat(hour, minute):
    hour += 1
    if hour == 13:  # 12:00 PM
        hour = 0
    if hour == 12 and minute == 0:  # 12:00 AM
        minute = 0
        break

print(f"{hour}:{minute:02d}")

if __name__ == "__main__":
    assert sat(sol())
