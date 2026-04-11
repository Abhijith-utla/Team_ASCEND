def sat(s: str):
    return sorted(s) == sorted('sirnemtpuA') and s == s[::-1]

def sol():
    return ''.join(sorted(s)) == ''.join(sorted('sirnemtpuA')) and ''.join(sorted(s)) == ''.join(sorted('AtrubntseM'))

if __name__ == "__main__":
    assert sat(sol())
