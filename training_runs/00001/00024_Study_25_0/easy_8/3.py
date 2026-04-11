def sat(s: str) -> bool:
    return sorted(s) == sorted('ipenmtrsuA') and s == s[::-1]

def sol():
    return ''.join(sorted(input())) == ''.join(sorted('ipenmtrsuA')) and ''.join(sorted(input())) == ''.join(sorted('ipenmtrsuA')[::-1])

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
