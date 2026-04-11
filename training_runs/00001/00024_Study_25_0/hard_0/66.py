def sat(s: str):
    return sorted(s) == sorted('Permute me true') and s == s[::-1]

def sol():
    return sorted(s) == sorted('Permute me true') and s == s[::-1]

if __name__ == "__main__":
    assert sat(sol())
