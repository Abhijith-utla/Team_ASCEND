def sat(hour: int, minute: int) -> bool:
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [90, 360 - 90]

def sol():
    hour = 12
    minute = 0
    while not sat(hour, minute):
        if minute == 59:
            hour += 1
            minute = 0
        else:
            minute += 1
    return {'hour': hour, 'minute': minute}

# checker
assert sat(sol()['hour'], sol()['minute'])

if __name__ == "__main__":
    assert sat(sol())
