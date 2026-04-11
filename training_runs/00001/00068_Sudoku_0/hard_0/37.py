def sat(x: str, puz="____9_2___7__________1_8_4____2_78____4_____1____69____2_8___5__6__3_7___49______"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    puz = "____9_2___7__________1_8_4____2_78____4_____1____69____2_8___5__6__3_7___49______"
    x = "_________982___7453186275__186427895928456173__5729638141284659739182746357896219__"
    assert sat(x)
    return x

print(sol())

if __name__ == "__main__":
    assert sat(sol())
