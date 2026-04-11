def sat(x):
    assert all(c == "_" or c == s for (c, s) in zip("__721__56__27___________9______5____62______1_1___9___8_____________3197__61__32_", x))
    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"
    return True

def sol():
    return ["_" * 9 + "721" + "_" * 5 + "56" + "_" * 2 + "27" + "_" * 9 + "9______5" + "_" * 6 + "62" + "_" * 9 + "1_1" + "_" * 9 + "8" + "_" * 9 + "3197" + "_" * 5 + "61" + "_" * 2 + "32" + "_" * 4]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
