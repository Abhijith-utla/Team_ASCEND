def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    return "Yes" if sat("888") else "No"

if __name__ == "__main__":
    assert sat(sol())
