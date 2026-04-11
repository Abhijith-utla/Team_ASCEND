def sat(s: str) -> bool:
    return s == '4.5abc' or s == '4.5abc. ' or s == ' 4.5abc.'

def sol():
    return '4.5abc'

if __name__ == "__main__":
    assert sat(sol())
