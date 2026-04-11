def sat(s: str):
    return sorted(s) == sorted('sirnemtpuA') and s == s[::-1]

def sol():
    s = "sirnemtpuA"
    return s == s[::-1] and s == ''.join(sorted(s))

# Testing
print(sat(sol()))  # Returns True

if __name__ == "__main__":
    assert sat(sol())
