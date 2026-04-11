def sat(li: List[str]):
    return sum([1 for i in li if ord(i) % 3 == 2]) == 0

def sol():
    return ord('a') % 3 == 2

def sat(li: List[str]):
    return sum([1 for i in li if ord(i) % 3 == 2]) == 0

# Test cases
print(sat([chr(i) for i in range(97, 123)]))  # True
print(sat([chr(i) for i in range(65, 91)]))  # False
print(sat(['a', 'b', 'c']))  # True
print(sat(['A', 'B', 'C']))  # False

if __name__ == "__main__":
    assert sat(sol())
