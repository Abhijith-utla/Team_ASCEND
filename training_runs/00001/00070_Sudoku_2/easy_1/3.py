def sat(x):
    assert all(c == "_" or c == s for (c, s) in zip("__721__56__27___________9______5____62______1_1___9___8_____________3197__61__32_", x))
    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"
    return True

def sol():
    x = ["_"] * 81
    def assign(row, col, num):
        if num not in row and num not in col and num not in box[3 * (col // 3) + row // 3]:
            x[row * 9 + col] = str(num)
            return True
        return False

    def solve(row, col):
        for num in range(1, 10):
            if assign(row, col, num):
                if row < 8 and col < 8:
                    if solve(row + 1, col):
                        return True
                if col < 8:
                    if solve(0, col + 1):
                        return True
        x[row * 9 + col] = "_"
        return False

    for k in range(9):
        box = [x[9 * k: 9 * k + 9] for i in range(3)]
        if not solve(0, k):
            return x
    return x

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
