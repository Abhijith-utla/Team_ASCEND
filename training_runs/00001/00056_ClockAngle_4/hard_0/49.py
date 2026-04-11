def sat(hands: List[int], target_angle=68):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return [0, 0]

# Correct pattern:
def sol():
    return [0, 0]

# Incorrect pattern:
def sol():
    return [13, 0]

# Correct pattern:
def sol():
    return [0, 30]

# Incorrect pattern:
def sol():
    return [0, 61]

# Correct pattern:
def sol():
    return [0, 120]

# Incorrect pattern:
def sol():
    return [1, 1]

# Correct pattern:
def sol():
    return [4, 59]

# Incorrect pattern:
def sol():
    return [12, 61]

# Correct pattern:
def sol():
    return [11, 0]

# Incorrect pattern:
def sol():
    return [12, 30]

# Correct pattern:
def sol():
    return [12, 0]

# Incorrect pattern:
def sol():

if __name__ == "__main__":
    assert sat(sol())
