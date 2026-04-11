def sat(hour: int, minute: int):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) == 360

def sol():
    return {"hour": 0, "minute": 0}

# Checker
def sat(answer):
    hour, minute = answer["hour"], answer["minute"]
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) == 360

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
