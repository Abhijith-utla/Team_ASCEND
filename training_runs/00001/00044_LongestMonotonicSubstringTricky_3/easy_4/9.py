def sat(x: int, y: int) -> bool:
    return x <= y

def sol():
    return None

assert sat(1, 2)
assert not sat(2, 1)
assert not sat(1, 1)
assert sat(0, 0)
assert not sat(100, 200)

if __name__ == "__main__":
    assert sat(sol())
