def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return "abc"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
