def sat(s: str):
    return len(set(s)) <= 2 and s == '1-8*+/6'

def sol():
    return '1-8*+/6'

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
