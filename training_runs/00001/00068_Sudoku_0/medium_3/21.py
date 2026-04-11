def sat(x: str, puz="____9_2___7__________1_8_4____2_78____4_____1____69____2_8___5_6__3_____7___49______"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    return """
    49_____8____2_7_____6____9____1_5_3_____7_2___6_____8_____5_1_____7_____9____2_____1_6_4_____3_5
    """

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
