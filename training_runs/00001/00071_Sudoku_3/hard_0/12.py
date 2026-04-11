def sat(x: str, puz="_____42______7_____4______9__49___626_8__3___3_7__65_4_5_3__1__1____8_7__________"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    return """
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [4, 5, 6, 7, 8, 9, 1, 2, 3]
    [7, 8, 9, 1, 2, 3, 4, 5, 6]
    [6, 7, 8, 1, 2, 3, 4, 5, 9]
    [5, 6, 7, 2, 3, 4, 9, 1, 8]
    [4, 9, 5, 3, 7, 6, 1, 2, 8]
    [3, 8, 4, 1, 5, 9, 2, 7, 6]
    [2, 9, 1, 8, 6, 7, 4, 3, 5]
    [1, 8, 2, 5, 4,

if __name__ == "__main__":
    assert sat(sol())
