def sat(s: str) -> bool:
    return sorted(s) == sorted('ipenmtrsuA') and s == s[::-1]

def sol():
    return ''.join(sorted(answer)) == ''.join(sorted('ipenmtrsuA')) and answer == answer[::-1]

if __name__ == "__main__":
    assert sat(sol())
