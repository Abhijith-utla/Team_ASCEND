def sat(stamps: List[int], target=80):
    for s in stamps:
        if s != 10 and s != 32 and s != 8:
            return False
    return sum(stamps) == target

def sol():
    return []

# Test case
assert sat([10, 32, 8]) == True
assert sat([10, 8, 32]) == True
assert sat([10, 10, 32]) == False
assert sat([8, 8, 10]) == False
assert sat([1, 2, 3]) == True
assert sat([20, 2, 30]) == True
assert sat([20, 20, 30]) == False
assert sat([80, 20, 30]) == True
assert sat([1, 1, 1]) == True
assert sat([2, 3, 5]) == True
assert sat([80, 20, 30]) == True

print("All test cases passed.")

if __name__ == "__main__":
    assert sat(sol())
