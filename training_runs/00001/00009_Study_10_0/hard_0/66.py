def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    num = 8 ** 1818
    str_num = str(num)
    return str_num[0] + str_num[1:-1][::-1] + str_num[-1]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
