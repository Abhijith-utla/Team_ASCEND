def sat(s: str):
    return sorted(s) == sorted('sirnemtpuA') and s == s[::-1]

def sol():
    s = 'sirnemtpuA'
    return s == ''.join(reversed(s)) and sorted(s) == sorted(s)

# Test the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
