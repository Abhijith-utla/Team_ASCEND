def sat(s: str):
    return sorted(s) == sorted('trusenipM') and s == s[::-1]

def sol():
    s = 'trusenipM'
    return sorted(s) == sorted(s) and s == s[::-1]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
