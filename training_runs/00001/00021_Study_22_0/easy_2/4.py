def sat(s: str) -> bool:
    return len(s) == 10 and s.isalpha() and '0' not in s and '1' not in s

def sol():
    s = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return sat(s)

if __name__ == "__main__":
    assert sat(sol())
