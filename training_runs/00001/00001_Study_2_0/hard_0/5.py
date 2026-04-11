def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

def sol():
    s = 'oo'*1000 + 'o' + 'ho'*800
    return s

# Test
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
