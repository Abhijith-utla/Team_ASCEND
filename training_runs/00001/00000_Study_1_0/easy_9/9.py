def sat(s: str):
    if s.count('o') != 0:
        return False
    return True

def sol():
    return "hello"

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
