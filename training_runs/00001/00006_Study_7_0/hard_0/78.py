def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    s = '8' * 8192
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

if __name__ == "__main__":
    assert sat(sol())
