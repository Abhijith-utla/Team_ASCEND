def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    num = 8 ** 1818
    str_num = str(num)
    return str_num == str_num[::-1] and len(str_num) > 11

if __name__ == "__main__":
    assert sat(sol())
