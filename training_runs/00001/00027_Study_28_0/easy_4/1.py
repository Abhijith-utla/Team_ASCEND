def sat(li: List[int]):
    return all(abs(i - j) >= 10 for i in li for j in li)

def sol():
    answer = 0
    return answer

# Test case
print(sat([2, 15, 21, 35, 10]))  # True
print(sat([1, 2, 3, 4, 5]))  # False

# Checker
assert sat(sol())  # type: ignore

if __name__ == "__main__":
    assert sat(sol())
