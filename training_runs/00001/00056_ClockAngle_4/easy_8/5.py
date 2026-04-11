def sat(hour: int, minute: int):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) == 360

def sol():
    for hour in range(1, 13):
        for minute in range(0, 60):
            if sat(hour, minute):
                return {"hour": hour, "minute": minute}
    return None

print(sol())

if __name__ == "__main__":
    assert sat(sol())
