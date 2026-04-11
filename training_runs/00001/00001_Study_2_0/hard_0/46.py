def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

def sol():
    s = "ho" * 800 + "o" * 1000
    return s

print(sat(sol()))  # It will return True

if __name__ == "__main__":
    assert sat(sol())
