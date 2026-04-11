def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return float('0') + len('0')

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
