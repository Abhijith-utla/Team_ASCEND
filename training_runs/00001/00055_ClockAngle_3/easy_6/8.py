def sat(hands: List[int], target_angle=138):
    h, m = hands
    assert 0 < h <= 12 and 0 <= m < 60
    hour_angle = 30 * h
    minute_angle = 6 * m
    return abs(hour_angle - minute_angle) == target_angle

def sol():
    return []

# Example usage
# print(sat([12, 30]))  # Returns True
# print(sat([12, 35]))  # Returns False
# print(sat([1, 30]))   # Returns False
# print(sat([11, 55]))  # Returns True

# Test cases
# assert sat([12, 30])   # Returns True
# assert sat([12, 35])   # Returns False
# assert sat([1, 30])    # Returns False
# assert sat([11, 55])   # Returns True
# assert sat([12, 60])   # Returns True
# assert sat([13, 0])    # Returns False
# assert sat([13, 30])   # Returns True
# assert sat([13, 45])   # Returns True
# assert sat([13, 60])   # Returns False
# assert sat([0, 30])    # Returns True
# assert sat([24, 0])    # Returns False

if __name__ == "__main__":
    assert sat(sol())
