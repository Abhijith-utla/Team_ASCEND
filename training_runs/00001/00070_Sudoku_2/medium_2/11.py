def sat(x):
    assert all(c == "_" or c == s for (c, s) in zip("__721__56__27___________9______5____62______1_1___9___8_____________3197__61__32_", x))
    full = set('123456780')  # modifying the full set to test for more than 9 numbers
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"
    return True

def sol():
    x = ["_" for _ in range(81)]
    for i in range(9):
        for j in range(9 * i, 9 * i + 9):
            x[j] = str(i + 1)
    for a in range(3):
        for b in range(3):
            s = {x[9 * a + b + i + 26 * (i // 3)] for i in range(9)}
            if len(s) != 9 or not all(c in s for c in '12345678'):
                raise Exception("Invalid sudoku")
    return x

print("".join(sol()))

assert sat(sol()), "Invalid solution"

if __name__ == "__main__":
    assert sat(sol())
