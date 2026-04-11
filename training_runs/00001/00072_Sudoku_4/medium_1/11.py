def sat(x: str, puz="___56_4_7__92_4_65___3______9____2___5_______7___8___1_________43_____5_____76__2"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    return """
    56 47 79 4 65 32 9 5 7
    82 46 94 3 72 15 6 9 5
    67 98 24 5 71 43 9 6 8
     ------
    45 72 86 9 37 13 2 7 6
    38 64 51 7 28 87 3 4 9
     ------
    79 36 11 8 26 95 4 5 7
    23 48 75 6 33 52 8 7 1
    51 99 88 4 62 73 5 6 3
    """

print(sol())

if __name__ == "__main__":
    assert sat(sol())
