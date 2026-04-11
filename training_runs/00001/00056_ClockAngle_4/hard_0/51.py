def sat(hands: List[int], target_angle=68):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return [], 0

assert sat(*sol())

def sol():
    return [0, 0], 0

assert sat(*sol())

def sol():
    return [12, 0], 12

assert sat(*sol())

def sol():
    return [11, 59], 11

assert sat(*sol())

def sol():
    return [11, 30], 30

assert sat(*sol())

def sol():
    return [12, 30], 60

assert sat(*sol())

def sol():
    return [11, 45], 45

assert sat(*sol())

def sol():
    return [12, 45], 90

assert sat(*sol())

def sol():
    return [11, 15], 15

assert sat(*sol())

def sol():
    return [12, 15], 30

assert sat(*sol())

def sol():
    return [1

if __name__ == "__main__":
    assert sat(sol())
