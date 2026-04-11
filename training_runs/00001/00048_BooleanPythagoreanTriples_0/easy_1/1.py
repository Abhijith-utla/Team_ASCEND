def sat(numbers: List[int], n=100):
    assert set(numbers) <= {0, 1}, 'Numbers must be in {0, 1}'
    assert len(numbers) >= n, 'Length of numbers must be greater than or equal to n'
    squares = {i ** 2: numbers[i] for i in range(1, len(numbers))}
    return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

def sol():
    return []

# Test cases
print(sat([1, 2, 3, 4, 5]))  # Expected to return False
print(sat([0, 0, 0, 0, 0]))  # Expected to return False
print(sat([1, 1, 1, 1, 1]))  # Expected to return True
print(sat([0, 1, 2, 3, 4]))  # Expected to return True
print(sat([0, 1, 2, 0, 1]))  # Expected to return False
print(sat([0, 0, 0, 1, 0]))  # Expected to return False
print(sat([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Expected to return False
print(sat([0, 0, 0, 0, 0, 1, 2, 3, 4, 5]))  # Expected to return False
print(sat([1

if __name__ == "__main__":
    assert sat(sol())
