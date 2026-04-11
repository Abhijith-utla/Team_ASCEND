def sat(hands):
    h, m = hands
    assert 0 <= h < 24 and 0 <= m < 60
    hour_angle = 30 * h + m / 6
    minute_angle = 6 * m
    return abs(abs(hour_angle - minute_angle) - 133) == 0

def sol():
    return {}

# Test cases
print(sat(sol()))  # True
print(sat(sol(12, 30)))  # False
print(sat(sol(15, 0)))  # False
print(sat(sol(23, 59)))  # False
print(sat(sol(0, 0)))  # False
print(sat(sol(12, 60)))  # False
print(sat(sol(24, 0)))  # False

# Checker function
assert sat(sol())  # True
assert not sat(sol(12, 30))  # False
assert not sat(sol(15, 0))  # False
assert not sat(sol(23, 59))  # False
assert not sat(sol(0, 0))  # False
assert not sat(sol(12, 60))  # False
assert not sat(sol(24, 0))  # False

if __name__ == "__main__":
    assert sat(sol())
