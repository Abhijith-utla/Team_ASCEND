def sat(li: List[int]):
    return all(li[i] < sum(li[:i+1]) for i in range(len(li)))

def sol():
    return sat([1, 2, 3, 4, 5])

def sat(li: List[int]):
    return all(li[i] < sum(li[:i+1]) for i in range(len(li)))

# Test cases
print(sat([1, 2, 3, 4, 5]))  # True
print(sat([5, 4, 3, 2, 1]))  # False
print(sat([1, 1, 1, 1, 1]))  # False
print(sat([10, 9, 8, 7, 6]))  # True
print(sat([1, 2, 3, 4, 5, 6]))  # False

if __name__ == "__main__":
    assert sat(sol())
