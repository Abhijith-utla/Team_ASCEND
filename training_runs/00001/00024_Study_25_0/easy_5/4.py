def sat(s: str):
    return sorted(s) == sorted('sirnemtpuAa') and s == s[::-1]

def sol():
    return "".join(sorted(s)) == "".join(sorted('sirnemtpuAa')) and "".join(sorted(s)) == "".join(reversed("sirnemtpuAa"))

if __name__ == "__main__":
    assert sat(sol())
