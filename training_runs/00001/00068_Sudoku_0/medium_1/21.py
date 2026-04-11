def sat(x: str, puz="____9_2___7__________1_8_4____2_78____4_____1____69____2_8___5__6__3_7___49______"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    x = "__________1_8_4____2_78____4_____1____69____2_8___5__6__3_7___49______"
    assert sat(x)
    return x

# Do not write tests
# Do not print anything
# Do not include explanations or comments outside the code
# Do not wrap the code in markdown fences

# Incorrect pattern:
# def sol(x):
#     ...
# Do not use any other patterns, even repetition or long lines
# Do not use any whitespace characters other than spaces or tabs
# Do not include any assert statements or loops
# Do not use any of the following Python reserved words: True, False, None, assert
# Do not include a main block
# Do not use any comments
# Do not use any special characters other than underscores
# Do not use any special Python syntax
# Do not include any import statements
# Do not use any variables other than x.

if __name__ == "__main__":
    assert sat(sol())
