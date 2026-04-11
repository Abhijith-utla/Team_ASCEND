def sat(colors, m):
    assert set(colors) <= {0, 1} and len(colors) >= m
    squares = {i: colors[i] for i in range(m)}
    return not any(c == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

def sol():
    return []

# Test cases
assert sat(sol(), 5) == [1, 0, 0, 0, 1]
assert sat(sol(), 6) == [1, 1, 1, 0, 0, 0]
assert sat(sol(), 7) == [1, 0, 1, 0, 0, 0, 0]
assert sat(sol(), 8) == [1, 1, 0, 1, 0, 0, 0, 0]
assert sat(sol(), 9) == [1, 0, 1, 0, 1, 0, 0, 0, 0]
assert sat(sol(), 10) == [1, 1, 0, 1, 0, 1, 0, 0, 0, 0]

if __name__ == "__main__":
    assert sat(sol())
