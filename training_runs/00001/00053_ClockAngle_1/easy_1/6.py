def sat(hands: List[int], target_angle=39):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == target_angle

def sol():
    return {"hands": [h, m]}

# Call the function to verify the solution
assert sat(sol()["hands"])

if __name__ == "__main__":
    assert sat(sol())
