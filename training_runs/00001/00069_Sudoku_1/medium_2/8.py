def sat(x: str, puz="__2__1_3__9_7_____5______8_6___5_______12____2____3_68________9_1_8__4____7____25"):
    assert all(c in ("_", "1", "2", "3", "5", "6", "7", "8") or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} <= full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} <= full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} <= full, "invalid square"

    return True

def sol():
    return """
    5______8_6__1__3_
    ____12_4______5
    __9_7_2_6_8__1_
    1_3_5_2_4_6_9_
    ______7_1_2_8_5
    4_6_8_5_3_1_7
    2_5_9_1_6_7_4_
    1_9_5_3_4_2_8_
    6_8_7_4_1_5_2_
    """.replace("_", "1").replace(" ", "")

print(f"Answer: {sol()}")

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
