def sat(x: str, puz="__2__1_3__9_7_____5______8_6___5_______12____2____3_68________9_1_8__4____7____25"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))
    return True

def sol():
    return "9_7_8_5_1_3_2_5_6_4_7_6_8_9_1_2_5_3_6_8_1_8_4_7_25"

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
