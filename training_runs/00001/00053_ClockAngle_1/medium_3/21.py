def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 <= h < 24 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# The answer object is a list, containing the hours and minutes of the clock.
def sol():
    return [[h, m] for h in range(24) for m in range(60)]

# The answer object is a list, containing the hours and minutes of the clock.
def sol():
    return [i for i in range(12)]

# The answer object is a string, containing the time in the format "HH:MM".
def sol():
    from datetime import datetime
    return datetime.now().strftime("%H:%M")

# The answer object is a list, containing the hours and minutes of the clock.
def sol():
    return [[h, m] for h in range(12) for m in range(60)]

# The answer object is an integer, representing the target angle of the clock.
def sol():
    return 39

if __name__ == "__main__":
    assert sat(sol())
