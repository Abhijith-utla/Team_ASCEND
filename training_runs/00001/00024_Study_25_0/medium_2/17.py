def sat(s: str):
    return sorted(s) == sorted('sirnemtpuA') and s == s[::-1]

def sol():
    return sorted(input()) == sorted('sirnemtpuA') and input() == input()[::-1]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
