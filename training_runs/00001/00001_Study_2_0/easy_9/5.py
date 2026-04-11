def sat(s: str):
    return s.count('m') == 400 and s.count('mm') == 401 and s.count('mmm') == 398

def sol():
    s = 'mmm' * 400 + 'mm' * 401
    return s

if __name__ == "__main__":
    assert sat(sol())
