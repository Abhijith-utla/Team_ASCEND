def sat(hour: int, minute: int) -> bool:
    hour_angle = 30 * hour + minute / 2
    minute_angle = 6 * minute
    return abs(hour_angle - minute_angle) in [68, 360 - 68]

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
