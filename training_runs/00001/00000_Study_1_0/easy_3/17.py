def sat(s: str):
    return 'oo' in s and s.count('o') <= 1000

def sol():
    s = input()
    if 'oo' in s and s.count('o') <= 1000:
        return True
    else:
        return False

if __name__ == "__main__":
    assert sat(sol())
