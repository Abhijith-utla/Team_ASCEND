def sat(colors):
    assert set(colors) <= {0, 1} and len(colors) >= 10000
    squares = {i: colors[i] for i in range(len(colors) // 2)}
    return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
