def sat(x: str, puz="__2__1_3__9_7_____5______8_6___5_______12____2____3_68________9_1_8__4____7____25"):
    assert all(c in ("_", "1", "2", "3") for c in x), "missing digits"
    return True

def sol():
    return "_213__97__5______86___5______12__2_3_68________918__4____7____25"

print(sol())

if __name__ == "__main__":
    assert sat(sol())
