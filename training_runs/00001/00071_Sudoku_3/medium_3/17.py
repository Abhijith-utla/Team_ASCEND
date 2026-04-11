def sat(x: str, puz="_____42_____7_____4_____9__49____626_8__3___3_7__65_4_5_3__1__1__8_7__________"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    return """
    123456789
    4_________
    __________
    __________
    __________
    __________
    __________
    __________
    8_________
    5_________
    3_________
    """

# Test case
# assert sat(sol())
print(sol())

if __name__ == "__main__":
    assert sat(sol())
