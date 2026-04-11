def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    s = "888"
    while not sat(s):
        s += "8"
    return s

if __name__ == "__main__":
    assert sat(sol())
