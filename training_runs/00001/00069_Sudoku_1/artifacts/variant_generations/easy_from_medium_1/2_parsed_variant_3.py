def sat(x: str, puz="__2__1_3__9_7_____5______8_6___5_______12____2____3_68________9_1_8__4____7____25"):
    assert all(c == s for c, s in zip(puz, x))
    return True

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
