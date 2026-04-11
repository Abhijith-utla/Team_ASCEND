def sat(x: str, puz="__2__1_3__9_7_____5______8_6___5_______12____2____3_68________9_1_8__4____7____25"):
    assert all(c == "_" or c == str(i) for i, c in enumerate("123456789", start=1)), f"invalid characters: {''.join(c for c in x if not c.isdigit())}"
    assert all(x[i] == str(i) for i in range(9)), f"invalid row: {''.join(x[i] for i in range(9))}"
    assert all(x[i+9] == str(i+1) for i in range(9)), f"invalid column: {''.join(x[i+9] for i in range(9))}"
    assert all(x[i+18] == str(i+9) for i in range(9)), f"invalid square: {''.join(x[i+18] for i in range(9))}"
    return True

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
