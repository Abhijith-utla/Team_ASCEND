def sat(x):
    full = set('123456789')
    for a in range(3):
        for b in range(3):
            assert {x[9 * a + b + i + 26 * (i % 3)] for i in range(9 * a, 9 * a + 9)} == full, "invalid square"
    return True

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
