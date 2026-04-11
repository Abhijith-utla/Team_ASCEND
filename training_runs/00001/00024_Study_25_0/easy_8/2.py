def sat(s: str) -> bool:
    return sorted(s) == sorted('ipenmtrsuA') and s == s[::-1]

def sol():
    return ''.join(sorted(input()))

def sat(s: str) -> bool:
    return sorted(s) == sorted('ipenmtrsuA') and s == s[::-1]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
