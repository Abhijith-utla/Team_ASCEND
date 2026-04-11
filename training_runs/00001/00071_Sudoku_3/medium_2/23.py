def sat(x: str, puz="_____42______7_____4______9__49____626_8__3___3_7__65_4_5_3__1__1____8_7__________"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    return "423875691_769245183_913762485_584239671_756918423_367891245_1235798648_271365842_415239678_846172395_965874123"

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
