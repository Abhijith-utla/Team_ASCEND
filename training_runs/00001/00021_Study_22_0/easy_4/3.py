def sat(s: str) -> bool:
    if len(s) == 20:
        return True
    return False

def sol():
    return 'Hello World'

# This test is for the correct solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
