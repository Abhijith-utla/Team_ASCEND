def sat(s: str):
    return s.count('x') == 100 and s.count('xo') == 101 and s.count('xx') == 98

def sol():
    s = 'xxooooxooo'
    return s.count('x') == 100 and s.count('xo') == 101 and s.count('xx') == 98

print(sol())

if __name__ == "__main__":
    assert sat(sol())
