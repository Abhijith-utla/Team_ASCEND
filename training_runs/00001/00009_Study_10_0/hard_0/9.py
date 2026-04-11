def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol(s: str) -> bool:
    return s in '81818181818181818181' and s == s[::-1] and len(s) > 11

if __name__ == "__main__":
    assert sat(sol())
