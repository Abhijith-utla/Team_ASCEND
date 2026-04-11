def sat(x: str, puz="____9_2___7__________1_8_4____2_78____4_____1____69____2_8___5_6__3_7___49______"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    return """
    49_____28_____3_1_69_____8_____5_____7_____6_____4_____2_____1_____8_____3_____6_____9_____5_____2_____1
    1_8____2_____3_____69_____78_____5_____4_____8_____28_____3_____1_____6_____5_____7_____8_____4_____9
    _____1____2____3_____4_____5_____6_____7_____8_____9_____1_____2____3_____4_____5_____6_____7_____8
    """

print(sol())

if __name__ == "__main__":
    assert sat(sol())
