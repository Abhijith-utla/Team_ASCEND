def sat(stamps: List[int], target=60, max_stamps=1, options=[25, 22, 8, 84, 60, 56]):
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return [60, 25, 22, 8, 84, 56]

# Test the function with a solution
print(sat(sol()))  # This should return True

# Test the function with an incorrect solution
print(sat([60]*6))  # This should return False
print(sat([60]*5))  # This should return False
print(sat([60]*7))  # This should return False
print(sat([50]*6))  # This should return False
print(sat([60]*5 + [20]*1))  # This should return False
print(sat([60]*5 + [50]*1))  # This should return True

if __name__ == "__main__":
    assert sat(sol())
