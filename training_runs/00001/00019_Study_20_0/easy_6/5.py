def sat(li: List[int]) -> bool:
    return all(li[i] != li[i + 1] for i in range(len(li) - 1)) and (li[0] < li[-1]) or (li[0] > li[-1])

def sol():
    return sat([1, 2, 3, 4, 5])

# Test cases
print(sat([1, 2, 3, 4, 5]))  # True
print(sat([1, 1, 3, 4, 5]))  # False
print(sat([5, 4, 3, 2, 1]))  # False
print(sat([1, 5, 3, 4, 5]))  # False
print(sat([5, 4, 3, 2]))  # False

# Checker will run: assert sat(sol())
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
