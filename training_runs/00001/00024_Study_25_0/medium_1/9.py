def sat(s: str):
    return sorted(s) == sorted('trusenipM') and s == s[::-1]

def sol():
    s = 'trusenipM'
    return s == ''.join(sorted(s)) and s == ''.join(sorted(s)[::-1])

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
