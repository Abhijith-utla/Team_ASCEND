def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h + m / 2
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == target_angle

def sol():
    return []

# Incorrect case
def sol_incorrect_case():
    return [1, 2]

# Incorrect hour case
def sol_incorrect_hour_case():
    return [13, 2]

# Incorrect minute case
def sol_incorrect_minute_case():
    return [11, 62]

# Correct case
def sol_correct_case():
    return [11, 30]

# Test cases
assert sat(sol_correct_case())
assert not sat(sol_incorrect_case())
assert not sat(sol_incorrect_hour_case())
assert not sat(sol_incorrect_minute_case())

if __name__ == "__main__":
    assert sat(sol())
