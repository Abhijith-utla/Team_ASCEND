def sat(hour: int, minute: int):
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) == 0

def sol():
    for hour in range(12):
        for minute in range(60):
            if sat(hour, minute):
                return hour, minute
    return None

# Testing
hour, minute = sol()
print(f"{hour}:{minute}")

if __name__ == "__main__":
    assert sat(sol())
