def sat(x: str, puz="__2__1_3__9_7_____5______8_6___5_______12____2____3_68________9_1_8__4____7____25"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    return """
    9 8 7 6 5 4 3 2 1
    --------------------
    1 2 3 4 5 6 7 8 9
    --------------------
    7 6 5 4 3 2 1 8 9
    --------------------
    5 6 7 8 1 2 3 4 9
    --------------------
    3 4 5 6 7 8 9 1 2
    --------------------
    6 5 4 3 2 1 8 7 9
    --------------------
    8 6 5 4 3 2 1 9 2
    --------------------
    7 8 9 1 2 3 4 5 6
    """

if __name__ == "__main__":
    assert sat(sol())
