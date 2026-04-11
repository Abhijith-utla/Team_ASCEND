def sat(x: str, puz="_____42______7_____4______9__49____626_8__3___3_7__65_4_5_3__1__1____8_7__________"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    return """
        8 ___ 9 __ 3 ___ 5 __ 7 ___ 1 ___ 6 ___ 4
        2 ___ 1 __ 5 ___ 7 __ 4 ___ 8 ___ 3 ___ 6
        6 ___ 7 __ 2 ___ 8 __ 1 ___ 4 ___ 5 ___ 3

        4 ___ 5 __ 8 ___ 1 ___ 7 ___ 2 ___ 6 ___ 9
        3 ___ 4 __ 6 ___ 5 ___ 8 ___ 7 ___ 1 ___ 4
        7 ___ 1 ___ 2 ___ 9 ___ 4 ___ 5 ___ 6 ___ 8

        9 ___ 6 ___ 1 ___ 8 ___ 5 ___ 2 ___ 7 ___ 4
        5 ___ 8 ___ 4 ___ 2 ___ 1 ___ 6 ___ 9 ___ 7
        1 ___ 7

if __name__ == "__main__":
    assert sat(sol())
