def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return float(str(len("str"))) + len("str") == 4.5

if __name__ == "__main__":
    assert sat(sol())
