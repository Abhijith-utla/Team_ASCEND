def sat(colors):
    assert set(colors) <= {0, 1} and len(colors) >= 7824
    squares = {i ** 2: i for i in range(len(colors))}
    return not any(c == squares.get(i + j) for i, c in squares.items())

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
