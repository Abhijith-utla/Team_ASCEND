def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

def sol():
    s = "ho" * 801 + "oo" * 100 + "o" * 1000
    return s

if __name__ == "__main__":
    assert sat(sol())
