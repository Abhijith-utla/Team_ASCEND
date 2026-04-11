def sat(s: str):
    return sorted(s) == sorted('uipenmtrsA') and s == s[::-1]

def sol():
    return "".join(sorted(s)) == "".join(sorted('uipenmtrsA')) and "".join(sorted(s)) == "".join(sorted(reversed(s)))

if __name__ == "__main__":
    assert sat(sol())
