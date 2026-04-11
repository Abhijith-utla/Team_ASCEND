def sat(s: str):
    return s.count('z') == 100 and s.count('zo') == 101 and s.count('zz') == 98

def sol():
    return 'z' * 100 + 'zo' * 101 + 'zz' * 98

print(sol())

if __name__ == "__main__":
    assert sat(sol())
