def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    return "True" if sat("88888") else "False"

assert sol() == "True"

if __name__ == "__main__":
    assert sat(sol())
