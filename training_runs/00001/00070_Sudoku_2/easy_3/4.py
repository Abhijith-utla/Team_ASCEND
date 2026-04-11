def sat(x):
    full = set('123456789')
    for a in range(3):
        for b in range(3):
            assert {x[9 * a + b + i + 26 * (i % 3)] for i in range(9 * a, 9 * a + 9)} == full, "invalid square"
    return True

def sol():
    return {
        0: 1,
        1: 2,
        2: 3,
        3: 4,
        4: 5,
        5: 6,
        6: 7,
        7: 8,
        8: 9
    }

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
