def sat(s: str):
    return sorted(s) == sorted('trusenipM') and s == s[::-1]

def sol():
    return ''.join(sorted('trusenipM'))

if __name__ == "__main__":
    assert sat(sol())
