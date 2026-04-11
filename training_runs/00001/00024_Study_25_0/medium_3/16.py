def sat(s: str):
    return sorted(s) == sorted('uipenmtrsA') and s == s[::-1]

def sol():
    return sorted(''.join(filter(str.isalpha, 'uipenmtrsA'))) == sorted(''.join(filter(str.isalpha, 'uipenmtrsA'[::-1])))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
