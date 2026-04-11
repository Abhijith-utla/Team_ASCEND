def sat(x: str, puz="____9_2___7__________1_8_4____2_7_8____4_____1____69_2_8__5_6__3_7___49______"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    puz = "____9_2___7__________1_8_4____2_7_8____4_____1____69_2_8__5_6__3_7___49______"
    x = "92184271_6928541_71_346928571_5_8_271928465_7_4_218569347_2_1_792846518_8_6_518739246_9_4_218569347_2_1_792846518_8_6_518739246_9_4_218569347_2_1_792846518_8_6_518739246_9_4_218569347_2_1_792846518

if __name__ == "__main__":
    assert sat(sol())
