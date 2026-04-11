def sat(s: str):
    return sorted(s) == sorted('sirnemtpu') and s == s[::-1]

def sol():
    return ''.join(sorted(s)) == ''.join(sorted('sirnemtpu')) and ''.join(sorted(s)) == ''.join(sorted('snirntempu'))

if __name__ == "__main__":
    assert sat(sol())
