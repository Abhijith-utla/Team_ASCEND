def sat(s: str):
    return s.count('m') == 400 and s.count('mm') == 401 and s.count('mmm') == 398

def sol():
    s = 'mmm' * 3990
    return s

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
