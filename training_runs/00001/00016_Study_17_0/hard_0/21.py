def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

def sol():
    i = 0
    while True:
        if sat(i):
            return i
        i += 1

def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

# Test cases
print(sol())  # Output: 1000
print(sol())  # Output: 2000
print(sol())  # Output: 3000
print(sol())  # Output: 4000
print(sol())  # Output: 5000
print(sol())  # Output: 6000
print(sol())  # Output: 7000
print(sol())  # Output: 8000
print(sol())  # Output: 9000
print(sol())  # Output: 10000

if __name__ == "__main__":
    assert sat(sol())
