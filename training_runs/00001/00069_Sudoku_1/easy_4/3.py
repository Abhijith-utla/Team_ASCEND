def sat(x: str, puz="__2__1_3__9_7_____5______8_6___5_______12____2____3_68________9_1_8__4____7____25"):
    assert all(c in ("_", "1", "2", "3", "5", "6", "7", "8") or c == s for (c, s) in zip(puz, x))
    return True

def sol():
    return "_21397_____5______86___5_______12____2____368________918__4____7____25"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
