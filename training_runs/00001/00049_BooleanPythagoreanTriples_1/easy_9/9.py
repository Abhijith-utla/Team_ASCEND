def sat(colors):
    assert set(colors) <= {0, 1} and len(colors) >= 5000
    squares = {i: colors[i] for i in range(1, len(colors))}
    return not any(c == d for a, c in squares.items() for b, d in squares.items() if a != b)

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
