def sat(s: str):
    return s.count('z') == 100 and s.count('zo') == 101 and s.count('zz') == 98

def sol():
    return 'zo'*100 + 'z'*101

if __name__ == "__main__":
    assert sat(sol())
