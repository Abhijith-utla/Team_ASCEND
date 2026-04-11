def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return len(str(4.5))

assert sat(str(sol()))

if __name__ == "__main__":
    assert sat(sol())
