def sat(hands: Tuple[int, int]):
    h, m = hands
    assert 0 <= h < 24 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [38, 360 - 38]

def sol():
    return (hour, minute)

Incorrect pattern:
def sol(x):
    hour, minute = x
    assert 0 <= hour < 24 and 0 <= minute < 60
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [38, 360 - 38]

if __name__ == "__main__":
    assert sat(sol())
