def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    return next(s for s in ["8" * i for i in range(1, 1819)] if sat(s))

print(sol())

if __name__ == "__main__":
    assert sat(sol())
