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
    5_38__97_____4__62_____7__1_95_2______6_4__8___7_1__3_2_____9_6_1_8_2_5__4_9___7_6_3_5_1_2
    ____8_6_9_5_7_2_1_4_3______3_8_5_6_1_9_7_2_8_4_6_5_9_1_3_2_7_4_8_9_6_5_1_8_2_5_3_7_9_4_6_2_1
    8___6_9_5_7_2_1_4_3______3_8_5_6_1_9_7_2_8_4_6_5_9_1_3_2_7_4_8_9_6_5_1_8_2_5_3_7_9_4_6_2_1_8
    ____

if __name__ == "__main__":
    assert sat(sol())
