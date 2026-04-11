def sat(stamps: List[int], target=80, max_stamps=4):
    if len(stamps) > max_stamps:
        return False
    return sum(stamps) == target

def sol():
    return []

# Testing the function
assert sat([]) == False
assert sat([10, 20]) == False
assert sat([30]) == False
assert sat([30, 30]) == True
assert sat([10, 20, 30, 30]) == True
assert sat([10, 20, 30, 30, 10]) == False

if __name__ == "__main__":
    assert sat(sol())
