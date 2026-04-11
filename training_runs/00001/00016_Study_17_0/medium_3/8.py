def sat(i: int):
    return len(str(i + 1000)) < len(str(i + 1001))

def sol():
    i = 0
    while sat(i):
        i += 1
    return i

# Test cases
print(sat(1))  # True
print(sat(10))  # False
print(sat(100))  # True
print(sat(1000))  # False
print(sat(9999))  # True

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
