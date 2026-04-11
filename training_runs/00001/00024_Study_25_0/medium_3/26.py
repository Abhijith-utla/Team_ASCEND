def sat(s: str):
    return sorted(s) == sorted('uipenmtrsA') and s == s[::-1]

def sol():
    return ''.join(sorted(s)) == ''.join(sorted('uipenmtrsA')) and ''.join(sorted(s)) == ''.join(sorted('uipenmtrsA')[::-1])

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
