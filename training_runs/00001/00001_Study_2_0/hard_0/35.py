def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

def sol():
    return 'Hello, World!'

if __name__ == "__main__":
    assert sat(sol())
