def sat(hour: int, minute: int):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) == 360

def sol():
    for hour in range(1, 13): # 12 hours, 0-11
        for minute in range(0, 60): # 60 minutes, 0-59
            if sat(hour, minute):
                return {"hour": hour, "minute": minute}
    return None

# Assertion
assert sat(sol()["hour"], sol()["minute"])

if __name__ == "__main__":
    assert sat(sol())
