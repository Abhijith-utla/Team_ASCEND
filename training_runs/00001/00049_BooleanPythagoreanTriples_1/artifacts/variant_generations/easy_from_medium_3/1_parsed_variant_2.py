def sat(colors):
    assert set(colors) <= {0, 1} and len(colors) >= 5000
    squares = [(i ** 2, colors[i]) for i in range(1, len(colors))]
    return not any(c == d for a, c in squares for b, d in squares if a != b and c == d)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
