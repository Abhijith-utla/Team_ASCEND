def sat(s: str):
    return sorted(s) == sorted('sirnemtpuAa') and s == s[::-1]

def sol():
    return ''.join(sorted(input())) == ''.join(sorted('sirnemtpuAa')) and ''.join(sorted(input())) == ''.join(sorted('sirnemtpuAa')[::-1])

if __name__ == "__main__":
    assert sat(sol())
