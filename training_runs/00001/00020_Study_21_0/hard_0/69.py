def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    return []

# Test cases
assert sat([]) == False
assert sat([1]) == False
assert sat([1, 1]) == False
assert sat([1, 2]) == True
assert sat([2, 1]) == True
assert sat([2, 2]) == False
assert sat([1, 2, 3]) == True
assert sat([1, 2, 2]) == False
assert sat([1, 3, 2]) == False
assert sat([3, 1, 2]) == False

# Fully constructed solution
def sol():
    return [1, 2, 3]

# Checker
def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

if __name__ == "__main__":
    assert sat(sol())
