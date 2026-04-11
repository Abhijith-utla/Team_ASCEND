def sat(colors: List[int], n=1):
    assert set(colors) <= {0, 1} and len(colors) >= n
    squares = {i ** 2: colors[i] for i in range(1, len(colors))}
    return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

def sol():
    return {0, 1}

# Test cases
assert sat(list(sol()))
assert not sat(list(sol()))
assert sat(list(sol([0, 1, 0, 1, 0, 1, 0, 1])))
assert not sat(list(sol([0, 1, 0, 1, 0, 1, 0, 1, 0])))
assert not sat(list(sol([0, 0, 0, 0, 0, 0, 0, 0])))
assert sat(list(sol([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,

if __name__ == "__main__":
    assert sat(sol())
