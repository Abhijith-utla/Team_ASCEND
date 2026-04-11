def sat(s: str) -> bool:
    return sorted(s) == sorted('ipenmtrsuA') and s == s[::-1]

def sol():
    return ''.join(sorted(s)) == ''.join(sorted('ipenmtrsuA')) and ''.join(sorted(s)) == ''.join(sorted('Atrnmsip'))

if __name__ == "__main__":
    assert sat(sol())
