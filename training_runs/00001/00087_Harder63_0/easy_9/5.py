def sat(s: str):
    return len(set(s)) < 3 and s == '1-8*+/6'

def sol():
    return '0'

if __name__ == "__main__":
    assert sat(sol())
