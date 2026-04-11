def sat(hour: int, minute: int, target_angle = 68):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return {
        'hour': 0,
        'minute': 0,
    }

assert sat(sol()['hour'], sol()['minute'])

if __name__ == "__main__":
    assert sat(sol())
