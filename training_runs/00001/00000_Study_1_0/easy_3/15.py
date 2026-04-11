def sat(s: str):
    return 'oo' in s and s.count('o') <= 1000

def sol():
    return "oo" in "ooo" and "o" not in "ooo" and "oo" in "oo" and "o" not in "oo" and "o" not in "ooo" and "o" not in "oo" and "oo" in "oo" and "o" not in "oo" and "o" in "oo" and "o" not in "oo" and "o" not in "ooo" and "o" in "oo" and "o" not in "oo" and "o" not in "oo" and "o" in "oo" and "ooo" in "ooo" and "o" not in "oo" and "o" not in "oo" and "o" in "oo" and "o" in "oo" and "oo" not in "oo" and "oo" not in "oo" and "ooo" in "ooo" and "oo" in "oo" and "oo" in "oo" and "oo" not in "oo" and "oo" not in "

if __name__ == "__main__":
    assert sat(sol())
