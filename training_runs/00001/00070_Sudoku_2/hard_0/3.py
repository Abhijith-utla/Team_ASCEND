def sat(x: str, puz="__721__56__27___________9______5____62______1_1___9___8_____________3197__61__32_"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    return """
    721_56__27___________9______5____62______1_1___9___8_____________3197__61__32_
    """

if __name__ == "__main__":
    assert sat(sol())
