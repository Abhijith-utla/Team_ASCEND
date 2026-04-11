def sat(colors: List[int], n=100):
    assert set(colors) <= {0, 1}, 'Colors must be in {0, 1}'
    assert len(colors) >= n, 'Length of colors must be greater than or equal to n'
    squares = {i ** 2: colors[i] for i in range(1, len(colors))}
    return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

def sol():
    return []

# Test cases
assert sat([]) == False
assert sat([1]) == False
assert sat([0] * 99) == False
assert sat([0] * 100 + [1]) == False
assert sat([0] * 101) == False
assert sat([0] * 99 + [1]) == False
assert sat([0] * 99 + [1] * 100) == False
assert sat([1] * 100) == False
assert sat([0] * 99 + [1] * 100 + [0]) == True

if __name__ == "__main__":
    assert sat(sol())
