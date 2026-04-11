def sat(numbers: List[int], n=2):
    assert len(numbers) >= n
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-n))

def sol():
    return []

# Test cases
assert sat([]) == False
assert sat([1]) == False
assert sat([1, 2]) == True
assert sat([1, 2, 3]) == True
assert sat([1, 2, 2]) == False
assert sat([1, 2, 3, 4, 5]) == True
assert sat([1, 2, 3, 4, 5, 6]) == False
assert sat([1, 2, 3, 4, 5, 6, 7]) == False

# Additional test cases
assert sat([1, 2, 2, 3, 4, 5, 6, 7]) == False
assert sat([7, 6, 5, 4, 3, 2, 1]) == False

if __name__ == "__main__":
    assert sat(sol())
