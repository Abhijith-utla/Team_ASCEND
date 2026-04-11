def sat(x: str, puz="1___2___3______9____2___5_______7___8___1_________43_____5_____76__2___2___7___6___1___5_______7__8___9_______4_65___3______9____2___5_______7___8___1_________43_____5_____76__2"):
    assert all(c in "123" for c in x)

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"

def sol():
    return "123"*4 + "432"*4 + "765"*4 + "856"*4 + "967"*4 + "756"*4 + "843"*4 + "159"*4 + "654"*4 + "987"*4

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
