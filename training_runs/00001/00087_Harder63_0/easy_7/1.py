def sat(s: str):
    return len(set(s)) <= 1 and s == '1-8*+/6'

def sol():
    return '1-8*+/6'

if __name__ == "__main__":
    assert sat(sol())
