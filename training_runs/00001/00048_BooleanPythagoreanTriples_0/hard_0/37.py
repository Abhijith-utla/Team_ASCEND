def sat(colors: List[int], n=100):
    assert set(colors) <= {0, 1} and len(colors) >= n
    squares = {i ** 2: colors[i] for i in range(1, len(colors))}
    return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

def sol():
    return []

# Checker should fail because it's trying to test an empty list for "any" which is not applicable.
assert not sat([])

# Checker should fail because it's trying to test a list of length less than 100.
assert not sat([0]*99)

# Checker should pass because it's trying to test a list of length 100.
assert sat([0]*100)

if __name__ == "__main__":
    assert sat(sol())
