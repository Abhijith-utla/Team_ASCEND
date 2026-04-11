def sat(s: str):
    return sorted(s) == sorted('sirnemtpuA') and s == s[::-1]

def sol():
    return "".join(sorted(input("Enter a string: "))) == "".join(sorted('sirnemtpuA')[::-1]) and input("Enter a string: ") == input("Enter a string: ")[::-1]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
