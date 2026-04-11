def sat(li: List[int]):
    return all([i < li.index(x) + sum(li[:li.index(x)]) for x in set(li)])

def sol():
    return sat([1, 2, 3, 4, 5])

def sat(li: List[int]):
    return all([i < li.index(x) + sum(li[:li.index(x)]) for x in set(li)])

# Test cases
print(sat([1, 2, 3, 4, 5]))  # True
print(sat([5, 4, 3, 2, 1]))  # False
print(sat([1, 1, 1, 1, 1]))  # False
print(sat([1, 2, 3, 4, 5, 5, 5, 5]))  # False
print(sat([1, 2, 3, 4, 5, 5, 5, 5, 5, 5]))  # False

if __name__ == "__main__":
    assert sat(sol())
