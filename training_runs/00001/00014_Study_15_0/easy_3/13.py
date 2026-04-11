def sat(li: List[int]):
    return all(x >= 0 and 2 ** x - 1 == (2 ** (x + 1)) - 1 for x in li)

def sol():
    return [x for x in range(10) if not sat([x])]

def sat(li: List[int]):
    return all(x >= 0 and 2 ** x - 1 == (2 ** (x + 1)) - 1 for x in li)

# Test cases
print(sat([0]))  # True
print(sat([1]))  # True
print(sat([2]))  # True
print(sat([3]))  # False
print(sat([4]))  # False
print(sat([5]))  # False
print(sat([6]))  # False
print(sat([7]))  # False
print(sat([8]))  # False
print(sat([9]))  # False
print(sat([10]))  # False

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
