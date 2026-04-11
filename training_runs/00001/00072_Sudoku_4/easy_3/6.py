def sat(x: str, puz="___56_4_7__92_4_65___3______9____2___5_______7___8___1_________43_____5_____76__2"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))
    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + i + 26 * (i // 3)] for a in range(3)} == full, "invalid square"

    return True

def sol():
    x = "_____4_1_____5__3_6_8_7__9_2_7_4_3___2_6_8_5__1__6_4_9_7___8_5_2_1"
    return x

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
