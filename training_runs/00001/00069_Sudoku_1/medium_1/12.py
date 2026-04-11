def sat(x: str, puz="__2__1_3__9_7_____5______8_6___5_______12____2____3_68________9_1_8__4____7____25"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    puz = "__2__1_3__9_7_____5______8_6___5_______12____2____3_68________9_1_8__4____7____25"
    x = "_____________213__________97568__12_8_6_5_4_3_2_1_______859_7_6_4_3_2_1_9_8_7_6_5_4_3_2_1_8_9_7_6_5_4_3_2_1_7_8_9_6_5_4_3_2_1_6_8_9_7_6_5_4_3_2_1_5_8_9_7_6_5_4_3_2_1_4_8_9_7_6_5_4_3_2_1_3_8_9_7_6_5_4_3_2_1_2_8_9_7_6_5_4_3

if __name__ == "__main__":
    assert sat(sol())
