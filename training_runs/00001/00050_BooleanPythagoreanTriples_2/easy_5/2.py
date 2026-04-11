def sat(colors: List[int], n:int = 0):
    # Check if colors length is greater than or equal to n
    # Check if numbers in the list are 0 or 1
    # Check if there is any key in the squares dictionary where the sum is a key and the corresponding value is equal to the square of the sum.
    # If so, return True, else return False
    assert set(colors) <= {0, 1} and len(colors) >= n
    squares = {i ** 2: colors[i] for i in range(1, len(colors))}
    return not any(c == squares.get(i + j) for i, c in squares.items())

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
