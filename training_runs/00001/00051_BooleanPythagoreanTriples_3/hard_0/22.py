def sat(colors: List[int], n=1):
    assert set(colors) <= {0, 1} and len(colors) >= n
    squares = {i ** 2: colors[i] for i in range(1, len(colors))}
    return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

def sol():
    return []

# test cases
assert sat(sol())
assert not sat([0, 1, 0])
assert not sat([1, 0, 0])
assert not sat([1, 1, 1])
assert sat([0, 0, 0])
assert sat([0, 1, 1])
assert sat([0, 1, 0], 2)
assert not sat([0, 0, 1, 0])
assert sat([0, 0, 1])
assert sat([0, 0, 0, 0])
assert not sat([0, 1, 0, 1])
assert not sat([0, 1, 1, 0])

if __name__ == "__main__":
    assert sat(sol())
