def sat(s: str) -> bool:
    return sorted(s) == sorted('trusenipM') and s == s[::-1]

def sol():
    return ''.join(sorted(sorted('trusenipM'), reverse=True))

print(sol())

if __name__ == "__main__":
    assert sat(sol())
