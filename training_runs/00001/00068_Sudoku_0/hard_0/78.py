def sat(x: str, puz="____9_2___7__________1_8_4____2_78____4_____1____69____2_8___5__6__3_7___49______"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    return """
    5_8_1_3
    4_2_9_6
    7_6_0_1
    -------
    2_1_8_5
    6_7_0_4
    1_5_0_9
    -------
    8_4_0_2
    3_0_6_5
    6_8_0_7
    """

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
