def sat(s: str):
    return s.count('z') == 100 and s.count('zo') == 101 and s.count('zz') == 98

def sol():
    return 'zzzzzzzzzzo'

if __name__ == "__main__":
    assert sat(sol())
