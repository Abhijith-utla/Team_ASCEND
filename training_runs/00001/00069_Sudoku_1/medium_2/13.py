def sat(x: str, puz="__2__1_3__9_7_____5______8_6___5_______12____2____3_68________9_1_8__4____7____25"):
    assert all(c in ("_", "1", "2", "3", "5", "6", "7", "8") or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} <= full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} <= full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} <= full, "invalid square"

    return True

def sol():
    return """587_____6____251_____468_139_375_852_29_764_635_971____28_418_376_519_584_627_732_981_174_528_613_24_876_843_390_782_521_768_95_743_817_692_538_845_729_786_431_349_871_135_678_925_731_864_15_985_601_324_716_972_946_897_753_839_968_185_221_986_508_672_783_265_87

if __name__ == "__main__":
    assert sat(sol())
