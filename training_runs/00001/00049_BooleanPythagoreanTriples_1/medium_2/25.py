def sat(colors):
    assert set(colors) <= {0, 1} and len(colors) >= 10000
    squares = {i ** 2: colors[i] for i in range(1, len(colors))}
    return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

def sol():
    return {}

# Test the function with some input
assert sat({0} * 9999 + {1} * 1)
assert not sat({0} * 9999 + {1} * 10001)

# Test the function with some other input
assert not sat({0} * 9999 + {0} * 10000)
assert sat({0} * 9999 + {1} * 9999)

if __name__ == "__main__":
    assert sat(sol())
