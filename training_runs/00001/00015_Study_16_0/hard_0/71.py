def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return float(str(1234)) + len(str(1234)) == 4.5

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
