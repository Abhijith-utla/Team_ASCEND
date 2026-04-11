def sat(s: str):
    return sorted(s) == sorted('sirnemtpuA') and s == s[::-1]

def sol():
    return "".join(sorted(input()))

# Checker:
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
