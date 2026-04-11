def sat(x: str):
    assert all(c == "_" or c == s for (c, s) in zip(x, "____9_2___7__________1_8_4_____2_78____4_____1____69____2_8___5_6__3_____7___49______"))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    return "_" * 81

print(sol())

if __name__ == "__main__":
    assert sat(sol())
