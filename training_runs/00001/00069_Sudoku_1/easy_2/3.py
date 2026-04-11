def sat(x: str, puz="__2__1_3__9_7_____5______8_6___5_______12____2____3_68________9_1_8__4____7____25"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))
    return False

def sol():
    return "__2__1_3__9_7_____5______8_6___5_______12____2____3_68________9_1_8__4____7____25"

# Run the assertion
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
