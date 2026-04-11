def sat(x: str, puz="___56_4_7__92_4_65___3______9____2___5_______7___8___1_________43_____5_____76__2"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    puz = "___56_4_7__92_4_65___3______9____2___5_______7___8___1_________43_____5_____76__2"
    x = "__________82__________712345689__6__5__4__3_926578__8__1__7__5_4_3_____2_1___6_89__4"
    return x

print(sol())

if __name__ == "__main__":
    assert sat(sol())
