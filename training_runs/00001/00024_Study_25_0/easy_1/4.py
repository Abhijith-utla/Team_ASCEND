def sat(s: str) -> bool:
    return sorted(s) == sorted('trusenipM') and s == s[::-1]

def sol():
    return ''.join(sorted(s)) == ''.join(sorted('trusenipM')) and ''.join(sorted(s)) == ''.join(reversed('trusenipM'))

if __name__ == "__main__":
    assert sat(sol())
