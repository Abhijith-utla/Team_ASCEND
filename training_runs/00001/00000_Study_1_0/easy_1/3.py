def sat(s: str):
    return len(s) == 1000 and s.count('o') == 1000

def sol():
    return "hello" * 1000 + "o"

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
