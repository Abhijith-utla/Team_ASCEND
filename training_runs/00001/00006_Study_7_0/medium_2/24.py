def sat(s: str):
    return str(8 ** int(2888)).count(s) > 8 and len(s) == 3

def sol():
    return "888"

if __name__ == "__main__":
    assert sat(sol())
