def sat(stamps: List[int], target=80, max_stamps=4):
    if len(stamps) > max_stamps:
        return False
    return sum(stamps) == target

def sol():
    return []

# Test Case:
assert sat([10, 20, 30, 40]) == True
assert sat([10, 20, 30]) == False

# Check for the exception case
try:
    sat([10, 20, 30, 40, 50])
except Exception as e:
    assert type(e) == ValueError

if __name__ == "__main__":
    assert sat(sol())
