def sat(x):
    return all(x[i] <= x[i + 1] for i in range(len(x) - 1))

def sol():
    return [3, 2, 1]

# This assertion should pass.
assert sat(sol())

# This assertion should fail.
assert not sat(sol([3, 2]))

# This assertion should fail.
assert not sat(sol([1, 2, 3]))

# This assertion should pass.
assert sat(sol([1, 2, 2]))

if __name__ == "__main__":
    assert sat(sol())
