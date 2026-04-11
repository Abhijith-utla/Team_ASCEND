def sat(hour: int, minute: int) -> bool:
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [90, 360 - 90]

def sol():
    hour = 0
    while hour <= 12:
        minute = 0
        while minute <= 59:
            if sat(hour, minute):
                return hour, minute
            minute += 1
        hour += 1

# Test
answer = sol()
assert sat(answer[0], answer[1])

if __name__ == "__main__":
    assert sat(sol())
