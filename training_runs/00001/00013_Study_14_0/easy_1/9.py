def sat(li: List[int]):
    return all(li[i] < sum(li[:i]) for i in range(1, len(li)))

def sol():
    return sat([1, 2, 3, 4, 5])

def sat(li: List[int]):
    return all(li[i] < sum(li[:i]) for i in range(1, len(li)))

# Test cases
assert sat([1, 2, 3, 4, 5]) == True
assert sat([5, 4, 3, 2, 1]) == False
assert sat([1, 1, 1, 1, 1]) == False
assert sat([1]) == True
assert sat([]) == True

# Checker
def checker(answer):
    assert answer == True or answer == False

# Run the solution
checker(sol())

if __name__ == "__main__":
    assert sat(sol())
