def sat(x: str, puz="____9_2___7__________1_8_4____2_78____4_____1____69____2_8___5_6__3_7___49______"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[9 * i + i + i // 2] for i in range(3)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[i] for i in range(i // 3 * 27 + i % 3, i // 3 * 27 + i // 3 + 3)} == full, "invalid square"

    return True

def sol():
    return "182749653"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
