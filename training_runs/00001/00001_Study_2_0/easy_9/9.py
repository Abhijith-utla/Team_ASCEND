def sat(s: str):
    return s.count('m') == 400 and s.count('mm') == 401 and s.count('mmm') == 398

def sol():
    return not sat('m' * 400 + 'mm' * 401 + 'mmm' * 398)

if __name__ == "__main__":
    assert sat(sol())
