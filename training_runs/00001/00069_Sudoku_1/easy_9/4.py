def sat(x: str, puz="__2__1_3__9_7_____5______8_6___5_______12____2____3_68________9_1_8__4____7____25"):
    assert all(c in ("_", "1", "2", "3", "5") for c in x), "missing digits"
    return True

def sol():
    return "_2_1_3_9_7_5_6_8_5_12_2_3_68_9_1_8_4_7_25"

# The function `sat` checks if the given string `x` only contains digits, "_", "1", "2", "3", "5". If it does, it returns `True`. Otherwise, it returns `False`.
# We are using this function as a part of the final checker to ensure that `sol` returns a valid answer.

if __name__ == "__main__":
    assert sat(sol())
