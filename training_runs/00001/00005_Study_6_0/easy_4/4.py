def sat(i: int):
    return i % 5 == 0

def sol():
    return 20 // 5

# Check the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
