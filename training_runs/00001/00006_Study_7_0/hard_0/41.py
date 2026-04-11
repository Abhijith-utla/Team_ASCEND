def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    return "888" if sat("888") else "88"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
