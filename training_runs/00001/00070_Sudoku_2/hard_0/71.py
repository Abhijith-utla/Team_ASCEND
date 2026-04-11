def sat(x: str, puz="__721__56__27___________9______5____62______1_1___9___8_____________3197__61__32_"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    return ''.join(['_' * 81] + [str(i) for i in range(1, 10)] + [''.join(['_' * 27] + [str(i) for i in range(10, 19)] + [''.join(['_' * 36] + [str(i) for i in range(19, 28)]) + [''.join(['_' * 45] + [str(i) for i in range(28, 31)]) + [''.join(['_' * 54] + [str(i) for i in range(31, 34)]) + [''.join(['_' * 63] + [str(i) for i in range(34, 37)]) + [''.join(['_' * 72] + [str(i) for i in range(37, 40)]) + [''.join(['_' * 81] + [str(i) for i in range(40, 48)

if __name__ == "__main__":
    assert sat(sol())
