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
    9 6 8 3 1 7 5 4 2
    5 8 7 9 6 4 3 1 6
    4 3 6 1 8 2 7 5 9
    6 1 4 7 2 9 5 3 8
    8 7 9 5 1 3 6 4 2
    2 5 1 8 7 6 9 4 7
    7 4 2 3 8 1 6 9 5
    1 5 9 4 2 7 8 6 3
    3 6 7 2 9 8 5 1 4
    """

if __name__ == "__main__":
    assert sat(sol())
