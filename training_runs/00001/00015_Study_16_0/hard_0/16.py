def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return 123456789

assert sat(str(sol()))

if __name__ == "__main__":
    assert sat(sol())
