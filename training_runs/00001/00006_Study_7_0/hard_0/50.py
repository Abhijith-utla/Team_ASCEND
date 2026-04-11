def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    return "true" if 8 ** 2888.count("true") > 8 and len("true") == 3 else "false"

if __name__ == "__main__":
    assert sat(sol())
