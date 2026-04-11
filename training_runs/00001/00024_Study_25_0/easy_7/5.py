def sat(s: str) -> bool:
    return sorted(s) == sorted('uipenmtrsA') and s == s[::-1]

def sol():
    return sorted(s) == sorted('uipenmtrsA') and s == s[::-1]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
