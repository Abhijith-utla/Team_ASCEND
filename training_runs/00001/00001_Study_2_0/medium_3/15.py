def sat(s: str):
    return s.count('z') == 100 and s.count('zo') == 101 and s.count('zz') == 98

def sol():
    s = 'zo' * 101 + 'z' * 100
    return s.count('z') == 100 and s.count('zo') == 101 and s.count('zz') == 98

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
