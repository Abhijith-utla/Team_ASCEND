def sat(colors: List[int], n=7824):
    assert set(colors) <= {0, 1} and len(colors) >= n
    squares = {i ** 2: colors[i] for i in range(1, len(colors))}
    return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

def sol():
    return []

# assert sol([])
# assert sol([0, 1])
# assert sol([1, 0])
# assert sol([0, 0])
# assert sol([1, 1])
# assert sol([0, 1, 0])
# assert sol([1, 0, 1])
# assert sol([0, 1, 1])
# assert sol([1, 0, 0])

# assert not sol([0, 1])
# assert not sol([1, 0])
# assert not sol([0, 0])
# assert not sol([1, 1])
# assert not sol([0, 1, 0])
# assert not sol([1, 0, 1])
# assert not sol([0, 1, 1])
# assert not sol([1, 0, 0])

# assert sol(list(range(7824)))
# assert sol(list(range(7824, 0, -1)))
# assert sol(list(range(7823

if __name__ == "__main__":
    assert sat(sol())
