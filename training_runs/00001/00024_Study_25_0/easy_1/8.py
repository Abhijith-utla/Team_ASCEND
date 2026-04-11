def sat(s: str) -> bool:
    return sorted(s) == sorted('trusenipM') and s == s[::-1]

def sol():
    return ''.join(sorted(s for s in 'trusenipM' if s in 'trusenipM'))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
