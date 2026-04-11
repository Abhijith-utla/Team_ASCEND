def sat(s: str):
    return str(int(8 ** 2888)).count(s) == 8 and len(s) == 5

def sol():
    s = str(int(8 ** 2888))
    return s.count('8') == 8 and len(s) == 5

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
