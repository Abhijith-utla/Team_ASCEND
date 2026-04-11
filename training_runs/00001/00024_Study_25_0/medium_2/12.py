def sat(s: str):
    return sorted(s) == sorted('sirnemtpuA') and s == s[::-1]

def sol():
    return "".join(sorted(input())) == "".join(sorted('sirnemtpuA')) and "".join(input()) == "".join(reversed(input()))

if __name__ == "__main__":
    assert sat(sol())
