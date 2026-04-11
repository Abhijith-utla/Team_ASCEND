def sat(hands: List[int], target_angle=45):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

def sol():
    return []

# Do not modify the function body here.
# Instead, put your solution code in the function sol().

# The function sol() must have no arguments and must return a list of integers.
# The list should be empty in the first implementation.

# Please provide the solution code in the body of the function sol().

# For example, here is a possible implementation:
def sol():
    return []

# The function sol() must have no arguments and must return a list of integers.
# The list should be empty in the first implementation.

if __name__ == "__main__":
    assert sat(sol())
