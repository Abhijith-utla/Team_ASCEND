def sat(x: str, puz="___56_4_7__92_4_65___3______9____2___5_______7___8___1_________43_____5_____76__2"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))

    full = set('123456789')
    for i in range(9):
        assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
        assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
        assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"

    return True

def sol():
    puz = "___56_4_7__92_4_65___3______9____2___5_______7___8___1_________43_____5_____76__2"
    answer = ["_"] * 81
    for i in range(9):
        answer[i] = puz[i]
        answer[i + 9] = puz[i + 9]
        answer[i + 18] = puz[i + 18]
        answer[i + 27] = puz[i + 27]
        answer[i + 36] = puz[i + 36]
        answer[i + 45] = puz[i + 45]
        answer[i + 54] = puz[i + 54]
        answer[i + 63] = puz[i + 63]
        answer[i + 72] = puz[i + 72]
        answer[i + 80] = puz[i + 80]
    return answer

print(sol())

if __name__ == "__main__":
    assert sat(sol())
