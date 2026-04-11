def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return len("") + 1.5

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
