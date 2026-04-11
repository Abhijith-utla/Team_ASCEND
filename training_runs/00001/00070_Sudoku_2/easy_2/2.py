def sat(x):
    full = set('123456789')
    for i in range(9):
        assert {x[i], x[9 * i], x[9 * i + 1], x[9 * i + 2], x[9 * i + 3], x[9 * i + 4], x[9 * i + 5], x[9 * i + 6], x[9 * i + 7]} == full, "invalid row"
        assert {x[i], x[i + 9], x[i + 18], x[i + 27], x[i + 36], x[i + 45], x[i + 54], x[i + 63], x[i + 72]} == full, "invalid column"
    return True

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Correct pattern
assert sat(sol())
!

if __name__ == "__main__":
    assert sat(sol())
