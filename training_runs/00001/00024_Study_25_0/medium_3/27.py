def sat(s: str):
    return sorted(s) == sorted('uipenmtrsA') and s == s[::-1]

def sol():
    return ''.join(sorted(sorted(s) == sorted('uipenmtrsA') and s == s[::-1] for s in [input()])))

if __name__ == "__main__":
    assert sat(sol())
