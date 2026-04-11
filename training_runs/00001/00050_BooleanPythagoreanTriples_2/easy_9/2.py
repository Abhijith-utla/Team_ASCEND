def sat(colors, m):
    assert set(colors) <= {0, 1} and len(colors) >= m
    squares = {i: colors[i] for i in range(m)}
    return not any(c == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
