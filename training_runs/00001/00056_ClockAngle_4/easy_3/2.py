def sat(hand_position: float):
    hour_angle = 30 * (hand_position[0] % 12) + (hand_position[1] / 12)
    minute_angle = 6 * (hand_position[1])
    return abs(hour_angle - minute_angle) < 3

def sol():
    return []

# Checker function
def check_sol(sol_hand_position):
    hour_angle = 30 * (sol_hand_position[0] % 12) + (sol_hand_position[1] / 12)
    minute_angle = 6 * (sol_hand_position[1])
    return abs(hour_angle - minute_angle) < 3

# Test cases
test_cases = [[0, 0], [6, 0], [0, 6], [12, 0], [18, 0], [0, 12], [0, 18], [30, 0], [72, 0]]
for test in test_cases:
    assert check_sol(test), f"Failed for input: {test}"
print("All test cases passed")

# Main block
if __name__ == "__main__":
    main()

if __name__ == "__main__":
    assert sat(sol())
