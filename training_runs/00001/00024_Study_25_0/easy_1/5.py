def sat(s: str) -> bool:
    return sorted(s) == sorted('trusenipM') and s == s[::-1]

def sol():
    return ''.join(sorted(str(s))) == ''.join(sorted('trusenipM')) and str(s) == str(s)[::-1]

if __name__ == "__main__":
    assert sat(sol())
