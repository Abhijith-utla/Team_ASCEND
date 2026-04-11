def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return str(float("1") + len("1"))

if __name__ == "__main__":
    assert sat(sol())
