def sat(colors, n):
    assert set(colors) <= {0, 1} and len(colors) >= n
    squares = {i ** 2: colors[i] for i in range(n, len(colors))}
    return not any(c == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
