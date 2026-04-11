def sat(x: str, puz="_____42______7_____4______9__49___626_8__3___3_7__65_4_5_3__1__1____8_7__________"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    return "________42________7________4__________9________49________626________8__________3________3________7________65________4________5________3________1________1________8________7__________"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
