def sat(n: int):
    s = str(n * n)
    for i in "0123456789":
        assert s.count(i) == 1
    return True

def sol():
    return 1

# This assertion should fail because the square of 10 should yield 100, which is not a single number.
assert sat(sol())

# This assertion should pass because the square of 1 should yield 1, which is a single number.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
