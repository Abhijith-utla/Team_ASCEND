def sat(s: str):
    return sorted(s) == sorted('sirnemtpu') and s == s[::-1]

def sol():
    return ''.join(sorted(input())) == ''.join(sorted('sirnemtpu')) and ''.join(sorted(input())) == ''.join(sorted('sirnemtpu')[::-1])

if __name__ == "__main__":
    assert sat(sol())
