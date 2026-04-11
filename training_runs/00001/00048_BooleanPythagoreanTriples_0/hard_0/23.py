def sat(colors: List[int], n=100):
    assert set(colors) <= {0, 1} and len(colors) >= n
    squares = {i ** 2: colors[i] for i in range(1, len(colors))}
    return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

def sol():
    return []

# Testing the function with several test cases
print(sat([0, 1, 0, 1, 0, 1, 0, 1, 0, 1]))  # should return True
print(sat([1, 0, 1, 0, 1, 0, 1, 0, 1, 0]))  # should return False
print(sat([0, 1]))  # should return True
print(sat([1]))  # should return False
print(sat([0, 1, 0, 1]))  # should return False

# Ensure the function works with an argument
def sol(colors):
    return sat(colors)

# Testing the function with several test cases
print(sol([0, 1, 0, 1, 0, 1, 0, 1, 0, 1]))  # should return True
print(sol([1, 0, 1, 0, 1, 0, 1, 0, 1, 0]))  #

if __name__ == "__main__":
    assert sat(sol())
