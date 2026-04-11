def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return float(len(sol.__str__())) + 1 == 4.5

if __name__ == "__main__":
    assert sat(sol())
